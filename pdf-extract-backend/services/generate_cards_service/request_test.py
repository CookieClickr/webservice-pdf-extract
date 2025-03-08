import requests
import json

url = "http://127.0.0.1:5001/generate_cards"
headers = {"Content-Type": "application/json"}
data = {
    "markdown_text": "# Kapitel 1\n\nHier ist ein Beispieltext.\n\n## Unterkapitel\n\nMehr Inhalt..."
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Status Code:", response.status_code)
print("Response:", response.json())
