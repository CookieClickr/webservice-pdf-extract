import asyncio
import json
import os
from flask import Flask, request, jsonify
from openai import AsyncOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

# Lade die .env-Datei
load_dotenv()

# API-Key aus der Umgebung laden
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY ist nicht gesetzt. Bitte in der Umgebungsvariable hinterlegen.")

# OpenAI Async Client instanziieren
client = AsyncOpenAI(api_key=api_key)

# Maximale Zeichen pro Chunk
MAX_CHUNK_SIZE = 2000

app = Flask(__name__)


class Flashcard(BaseModel):
    title: str
    front: str
    back: str


def split_markdown(markdown_text: str, max_chunk_size: int = MAX_CHUNK_SIZE) -> list:
    sections = []
    current_section = []
    for line in markdown_text.splitlines():
        if line.startswith('# ') and current_section:
            sections.append("\n".join(current_section))
            current_section = [line]
        else:
            current_section.append(line)
    if current_section:
        sections.append("\n".join(current_section))

    final_chunks = []
    for section in sections:
        if len(section) <= max_chunk_size:
            final_chunks.append(section)
        else:
            paragraphs = section.split("\n\n")
            current_chunk = ""
            for para in paragraphs:
                if len(current_chunk) + len(para) + 2 <= max_chunk_size:
                    current_chunk = current_chunk + "\n\n" + para if current_chunk else para
                else:
                    if current_chunk:
                        final_chunks.append(current_chunk)
                    current_chunk = para
            if current_chunk:
                final_chunks.append(current_chunk)
    return final_chunks


def create_system_prompt() -> str:
    return """
Du bist ein Assistent, der aus einem gegebenen Markdown-Text Karteikarten generiert. Beachte folgende Anweisungen:

1) Erstelle Karteikarten im Format 'Frage: Antwort' mit klaren, abgeschlossenen Einheiten.
2) Inhaltsverzeichnisse, Metadaten zu Kursen oder Quellenverzeichnisse sind nicht relevant.
3) Jede Karteikarte hat einen Titel, eine Vorderseite und eine Rückseite.
4) Die Antwort erfolgt ausschließlich als JSON, IN GÜLTIGEM JSON FORMAT, ohne zusätzlichen Text.
Format:
{
  "title": "Titel der Karte",
  "front": "Frage/Problemstellung",
  "back": "Erklärung/Lösung"
} 
"""


def create_user_prompt(markdown_chunk: str) -> str:
    return f"""
### Hier ist der Markdown-Text:
{markdown_chunk}
"""


async def process_chunk(markdown_chunk: str):
    system_prompt = create_system_prompt()
    user_prompt = create_user_prompt(markdown_chunk)
    try:
        completion = await client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format=Flashcard,
        )
        flashcard = completion.choices[0].message
        if flashcard.refusal:
            return None
        else:
            return flashcard.parsed
    except Exception as e:
        return None


async def generate_cards(markdown_text: str):
    chunks = split_markdown(markdown_text)
    tasks = [process_chunk(chunk) for chunk in chunks]
    results = await asyncio.gather(*tasks)
    return [result for result in results if result is not None]


@app.route("/generate_cards", methods=["POST"])
def generate_flashcards():
    data = request.json
    if "markdown_text" not in data:
        return jsonify({"error": "Fehlende 'markdown_text' im Request"}), 400

    markdown_text = data["markdown_text"]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    flashcards = loop.run_until_complete(generate_cards(markdown_text))

    return jsonify([card.model_dump() for card in flashcards])

with open('static/swagger.yaml', 'r') as f:
    swagger_config = yaml.safe_load(f)

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flashcard Generator API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/swagger.json')
def swagger_json():
    return jsonify(swagger_config)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
