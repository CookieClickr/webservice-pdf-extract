# Zugriff auf den Service über den Docker-Hub

### Voraussetzungen
- Verbindung mit dem VPN der DHBW
- Zugangsdaten für den Portainer

### Schritte zur Nutzung des Flashcard-Generators

1. **Mit dem VPN der DHBW verbinden**
2. **Portainer öffnen:**  
   http://10.50.15.53:9000
3. **Mit den entsprechenden Zugangsdaten anmelden**
4. **Mit dem Server verbinden** und in der linken Navigation **„Stacks“** auswählen
5. Den Stack **„Flashcard-Generator“** auswählen
6. Auf das **Portmapping des Frontends (8080:5000)** klicken  
   → Das Frontend sollte sich im Browser öffnen
7. Auf die **Drag-and-Drop-Oberfläche** klicken, um eine PDF auszuwählen  
   - Empfehlung: die im Projekt enthaltene `test.pdf`, um lange Wartezeiten zu vermeiden
8. Nach dem Upload der PDF auf **„Analyse PDF“** klicken
9. Nach einer (hoffentlich kurzen) Wartezeit werden die **generierten Karteikarten** angezeigt
10. **Viel Spaß beim Lernen**

---

# Projekt Setup Anleitung Lokal

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
git clone https://github.com/CookieClickr/webservice-pdf-extract.git 
cd webservice-pdf-extract
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
## Zugriff auf die Swagger API

### Lokal

1. Nachdem das lokale Projekt aufgebaut wurde, ist die **Swagger API der einzelnen Services** unter  
   `http://localhost:<jeweiliger-Port>/swagger` erreichbar  
   (ersetze `<jeweiliger-Port>` mit dem Port des gewünschten Services)

### Auf dem Docker-Host

2. Auf dem Docker-Host ist die **Swagger UI** beispielhaft für den **Verwaltungsservice** implementiert und erreichbar unter:  
   [http://10.50.15.53:5004/swagger](http://10.50.15.53:5004/swagger)
