# Verwende ein schlankes, multi-arch Python-Image
FROM python:3.12-slim

# Installiere Git (und evtl. weitere notwendige Pakete)
RUN apt-get update && apt-get install -y libgl1-mesa-glx && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Setze das Arbeitsverzeichnis
WORKDIR /app


# Kopiere die Abhängigkeitsliste und installiere die Python-Pakete
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code in das Image
COPY . .

# Exponiere den Port, auf dem die Flask-App läuft (5001)
EXPOSE 5001

# Starte die Flask-Anwendung
CMD ["python", "app.py"]

