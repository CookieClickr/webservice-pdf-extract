from flask import Flask, request, send_from_directory, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import base64
import tempfile
import os
import requests
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # erlaubt standardmäßig alle Origins

# Swagger UI Konfiguration für Verwaltungs-Service
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Verwaltungs-Service API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/analyse-pdf', methods=['POST'])
def analyse_pdf():
    """
    1) Erwartet JSON: { "pdf": "<base64>" }
    2) Dekodiert das PDF und sendet es als Datei an /pdf-extract.
    3) Erhält 'markdown' und 'images' zurück.
    4) Für jedes Bild in 'images' ruft es /img-desc auf,
       erhält eine Beschreibung und ersetzt den Dateinamen im Markdown durch diese Beschreibung.
    5) Gibt das final angepasste Markdown zurück.
    """
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
                "http://pdf-extraction-service/pdf-extract",
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

        # Request an img-desc-service
        try:
            img_desc_response = requests.post(
                "http://img-desc-service/img-desc",
                json={"filename": filename, "data": base64_str}
            )
        except Exception as e:
            # Falls der Aufruf fehlschlägt
            desc = "Fehler bei Bildbeschreibung"
        else:
            if img_desc_response.status_code == 200:
                desc_data = img_desc_response.json()
                desc = desc_data.get("image_desc", {}).get(filename, {}).get("data", "")
                if not desc:
                    desc = "Keine Beschreibung verfügbar"
            else:
                desc = "Keine Beschreibung verfügbar"

        # Ersetze Bildname im Markdown durch Beschreibung (Regex für exakten Treffer)
        pattern = r"\b" + re.escape(filename) + r"\b"
        markdown = re.sub(pattern, desc, markdown)

    # Finales Markdown zurückgeben
    return jsonify({
        "markdown": markdown,
        "metadata": extract_data.get("metadata", {})
    }), 200

if __name__ == '__main__':
    # Port muss zum Kubernetes-Manifest passen (targetPort: 5000)
    app.run(host="0.0.0.0", port=5002)
