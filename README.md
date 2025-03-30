# Projekt Setup Anleitung

Dieses Projekt besteht aus zwei Hauptkomponenten:

- **Frontend**: Implementiert mit Node.js (npm).
- **Backend**: Mehrere Python Services, die in individuellen Service-Verzeichnissen liegen.

---

## Voraussetzungen

- Python 3.x
- Node.js und npm (empfohlene Version: LTS)

---

## 1. Repository klonen

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_VERZEICHNIS>
```

---

## 2. Backend einrichten

### Virtuelle Umgebung erstellen und aktivieren

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv venv
.env\Scriptsctivate
```

### Abhängigkeiten pro Service installieren

Navigiere nacheinander in jedes Backend-Service-Verzeichnis und installiere dort die Abhängigkeiten.

#### Linux / macOS

```bash
cd pdf-extract-backend/services/generate_cards_service
pip install -r requirements.txt

cd ../img_desc_service
pip install -r requirements.txt

cd ../pdf_extraction_service
pip install -r requirements.txt

cd ../verwaltungs_service
pip install -r requirements.txt

cd ../../..
```

#### Windows (PowerShell)

```powershell
cd pdf-extract-backend\services\generate_cards_service
pip install -r requirements.txt

cd ..\img_desc_service
pip install -r requirements.txt

cd ..\pdf_extraction_service
pip install -r requirements.txt

cd ..\verwaltungs_service
pip install -r requirements.txt

cd ..\..\..
```

---

## 3. Frontend einrichten

```bash
cd pdf-extract-frontend
npm install
```

---

## 4. Services starten

### Backend Services starten

Jeweils in neuem Terminal mit aktivierter virtueller Umgebung:

```bash
cd pdf-extract-backend/services/generate_cards_service
python app.py
```

```bash
cd pdf-extract-backend/services/img_desc_service
python app.py
```

```bash
cd pdf-extract-backend/services/pdf_extraction_service
python app.py
```

```bash
cd pdf-extract-backend/services/verwaltungs_service
python app.py
```

### Frontend starten

```bash
cd pdf-extract-frontend
npm run serve
```

Frontend ist dann erreichbar unter: [http://localhost:8080](http://localhost:8080)

---

## 5. Erster Test

Lade die Datei `test.pdf` im Frontend per Drag-and-Drop hoch.  
Dies dient als schneller Funktionstest und verhindert lange Wartezeiten bei größeren Dateien.

1. Browser öffnen: [http://localhost:8080](http://localhost:8080)
2. `test.pdf` ins Drag-and-Drop-Feld ziehen
3. Ergebnisse abwarten

---

Viel Erfolg 🚀
