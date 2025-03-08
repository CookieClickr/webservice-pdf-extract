from flask import Flask, request, send_from_directory, jsonify
import base64
import tempfile
import os
import requests
import re
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

app = Flask(__name__)
CORS(app)  # erlaubt standardmäßig alle Origins



@app.route('/analyse-pdf', methods=['POST'])
def analyse_pdf():
    data = request.get_json()
    if not data or 'pdf' not in data:
        return jsonify({"error": "Missing 'pdf' field in JSON payload"}), 400

    # PDF dekodieren
    try:
        pdf_bytes = base64.b64decode(data['pdf'])
    except Exception as e:
        return jsonify({"error": "Invalid Base64 for PDF", "details": str(e)}), 400

    # Temporäre Datei anlegen
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(pdf_bytes)
        temp_pdf_path = temp_pdf.name

    # PDF-Extraction-Service aufrufen
    try:
        with open(temp_pdf_path, 'rb') as f:
            files = {'file': f}
            pdf_extract_response = requests.post(
                "http://127.0.0.1:5003/pdf-extract",
                files=files
            )
    except Exception as e:
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
        return jsonify({"error": "Error calling PDF-Extraction-Service", "details": str(e)}), 500

    # Temporäre Datei löschen
    if os.path.exists(temp_pdf_path):
        os.remove(temp_pdf_path)

    if pdf_extract_response.status_code != 200:
        return jsonify({
            "error": "PDF Extraction Service error",
            "details": pdf_extract_response.text
        }), 500

    extract_data = pdf_extract_response.json()
    markdown = extract_data.get("markdown", "")
    images = extract_data.get("images", {})

    # Für jedes Bild den Image-Desc-Service aufrufen und Markdown ersetzen
    for filename, img_info in images.items():
        base64_str = img_info.get("data", "")

        try:
            img_desc_response = requests.post(
                "http://127.0.0.1:5002/describe_image",
                json={"filename": filename, "data": base64_str}
            )
        except Exception as e:
            desc = "Fehler bei Bildbeschreibung"
        else:
            if img_desc_response.status_code == 200:
                desc_data = img_desc_response.json()
                desc = desc_data.get("image_desc", {}).get(filename, {}).get("data", "Keine Beschreibung verfügbar")
            else:
                desc = "Keine Beschreibung verfügbar"

        pattern = r"\b" + re.escape(filename) + r"\b"
        markdown = re.sub(pattern, desc, markdown)

    # Aufruf des generate_cards_service
    try:
        generate_cards_response = requests.post(
            " http://127.0.0.1:5001/generate_cards",
            json={"markdown_text": markdown}
        )
    except Exception as e:
        return jsonify({"error": "Error calling Generate Cards Service", "details": str(e)}), 500

    if generate_cards_response.status_code != 200:
        return jsonify({
            "error": "Generate Cards Service error",
            "details": generate_cards_response.text
        }), 500

    flashcards = generate_cards_response.json()

    return jsonify({
        "flashcards": flashcards
    }), 200

with open('static/swagger.yaml', 'r') as f:
    swagger_config = yaml.safe_load(f)

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Central Control API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger_json():
    return jsonify(swagger_config)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)