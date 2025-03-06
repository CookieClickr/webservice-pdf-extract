import base64
import json
import requests

# Verwaltungsservice-URL
VERWALTUNGSSERVICE_URL = "http://localhost:5004/analyse-pdf"

# Pfad zur Test-PDF-Datei
PDF_FILE_PATH = "RA 08 X86.pdf"

# Funktion zum Laden und Kodieren der PDF-Datei in Base64
def encode_pdf_to_base64(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode("utf-8")

# PDF-Datei in Base64 umwandeln
encoded_pdf = encode_pdf_to_base64(PDF_FILE_PATH)

# JSON-Payload erstellen
payload = {"pdf": encoded_pdf}

# Anfrage an den Verwaltungsservice senden
response = requests.post(VERWALTUNGSSERVICE_URL, json=payload)

# Ergebnis ausgeben
if response.status_code == 200:
    result = response.json()
    print("Erhaltene Antwort:")
    print(json.dumps(result, indent=4, ensure_ascii=False))
else:
    print("Fehler beim Aufruf des Verwaltungsservices:")
    print(response.text)