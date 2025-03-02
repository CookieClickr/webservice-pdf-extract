from flask import Flask, request, send_from_directory, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger UI Konfiguration für Image-Description-Service
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Image-Description-Service API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/img-desc', methods=['POST'])
def img_desc():
    """
    Erwartet ein JSON im Format:
    {
      "filename": "page_0_Figure_3.jpeg",
      "data": "<base64-string>"
    }
    Gibt als Dummy-Antwort:
    {
      "image_desc": {
        "page_0_Figure_3.jpeg": {
          "data": "Beschreibung für page_0_Figure_3.jpeg"
        }
      }
    }
    """
    data = request.get_json()
    filename = data.get("filename", "unbekannt")
    # "data" ist der Base64-Inhalt, wird hier nicht weiterverarbeitet, da es ein Dummy ist

    # Erzeuge eine Dummy-Beschreibung
    description = f"Beschreibung für {filename}"

    return jsonify({
        "image_desc": {
            filename: {
                "data": description
            }
        }
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)
