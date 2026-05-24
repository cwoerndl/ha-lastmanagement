# Basis-Image: Offizielles HA OS Python-Image
FROM ghcr.io/hassio-addons/base/python:3.11-alpine

# Installiere System-Abhängigkeiten (für pip)
RUN apk add --no-cache py3-pip

# Kopiere requirements.txt und installiere Python-Pakete
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Kopiere Skripte und Konfiguration
COPY run.sh /run.sh
COPY lastmanagement.py /app/lastmanagement.py

# Setze Berechtigungen
RUN chmod +x /run.sh

# Setze Arbeitsverzeichnis
WORKDIR /app

# Starte das Add-on
CMD ["/run.sh"]