# Verwende ein schlankes, multi-arch Python-Image
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die Abhängigkeitsliste und installiere die Python-Pakete
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code in das Image
COPY . .

# Exponiere den Port, auf dem die Flask-App läuft (5002)
EXPOSE 5002

# Starte die Flask-Anwendung
CMD ["python", "app.py"]

