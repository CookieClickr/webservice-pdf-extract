import base64
import tempfile
import os
from flask import Flask, request, jsonify
from google import genai
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)


def save_temp_image(img_b64):
    image_data = base64.b64decode(img_b64)
    image = Image.open(BytesIO(image_data))

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        image.save(temp_file, format="JPEG")
        return temp_file.name


@app.route("/describe_image", methods=["POST"])
def describe_image():
    try:
        data = request.json
        if "filename" not in data or "data" not in data:
            return jsonify({"error": "Invalid input format"}), 400

        image_path = save_temp_image(data["data"])

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[
                'Describe this image in about 100 words.',
                Image.open(image_path)
            ]
        )

        os.remove(image_path)  # Temporäre Datei löschen

        return jsonify({
            "image_desc": {
                data["filename"]: {"data": response.text}
            }
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
