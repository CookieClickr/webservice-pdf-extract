from flask import Flask, request, send_from_directory, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.config.parser import ConfigParser
from PIL import Image
import os
from io import BytesIO
import base64
import json

app = Flask(__name__)

# Swagger UI Konfiguration für PDF-Extraction-Service
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "PDF-Extraction-Service API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Konfiguration für den PdfConverter
config = {
    "output_format": "markdown",
    "languages": "de",
    "use_fast": True
}
config_parser = ConfigParser(config)

converter = PdfConverter(
    config=config_parser.generate_config_dict(),
    artifact_dict=create_model_dict(),
    processor_list=config_parser.get_processors(),
    renderer=config_parser.get_renderer()
)

def serialize_image(image):
    """
    Konvertiert ein PIL.Image-Objekt in einen Base64-String und packt ihn in ein Dictionary
    mit dem Key 'data'.
    """
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")
    with BytesIO() as buffer:
        image.save(buffer, format="PNG")
        image_bytes = buffer.getvalue()
    base64_str = base64.b64encode(image_bytes).decode('utf-8')
    return {"data": base64_str}

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/pdf-extract', methods=['POST'])
def extract_pdf():
    """
    Verarbeitet eine hochgeladene PDF-Datei und gibt Markdown und Bilder (Base64) zurück.
    {
      "markdown": "Inhalt ...",
      "images": {
         "page_0_Figure_1.jpeg": {"data": "<base64>"},
         "page_1_Figure_2.jpeg": {"data": "<base64>"}
      }
    }
    """
    if 'file' not in request.files:
        return jsonify({"error": "Keine Datei im Request gefunden"}), 400

    pdf_file = request.files['file']
    if not pdf_file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Bitte eine PDF-Datei hochladen."}), 400

    temp_path = os.path.join('/tmp', pdf_file.filename)
    try:
        pdf_file.save(temp_path)
        rendered = converter(temp_path)
        if not rendered:
            return jsonify({"error": "Unbekanntes Ausgabeformat"}), 500

        # Bilder serialisieren
        img_dict = rendered.images
        serialized_images = {}
        if img_dict:
            for key, img in img_dict.items():
                if isinstance(img, Image.Image):
                    serialized_images[key] = serialize_image(img)
                else:
                    serialized_images[key] = {"data": ""}
        else:
            serialized_images = {}

        result = {
            "markdown": rendered.markdown,
            "metadata": rendered.metadata,
            "images": serialized_images
        }
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
