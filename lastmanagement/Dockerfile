# Basis-Image: Python 3.11 auf Alpine Linux
FROM homeassistant/amd64-base-python:3.11-alpine

# Installiere Abhängigkeiten
RUN apk add --no-cache py3-pip py3-yaml

# Installiere Python-Pakete (falls benötigt)
RUN pip install requests pyyaml

# Kopiere Skripte und Konfiguration
COPY run.sh /run.sh
COPY lastmanagement.py /app/lastmanagement.py

# Setze Berechtigungen
RUN chmod +x /run.sh

# Setze Arbeitsverzeichnis
WORKDIR /app

# Starte das Add-on
CMD ["/run.sh"]