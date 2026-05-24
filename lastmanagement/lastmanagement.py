#!/usr/bin/env python3
import argparse
import logging
import time
import json
import os
from homeassistant_api import Client

def main():
    # Argument-Parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="/data/options.json", help="Pfad zur Konfigurationsdatei")
    parser.add_argument("--log-level", default="info", help="Log-Level (debug, info, warning, error)")
    parser.add_argument("--interval", type=int, default=30, help="Aktualisierungsintervall in Sekunden")
    args = parser.parse_args()

    # Logging einrichten
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)
    logger.info("Starte Lastmanagement-Add-on...")

    # Konfiguration laden
    with open(args.config, "r") as f:
        config = json.load(f)
    logger.debug(f"Konfiguration: {config}")

    # Home Assistant API-Client initialisieren
    try:
        client = Client(
            os.getenv("SUPERVISOR_TOKEN"),
            os.getenv("HASSIO_API"),
        )
        logger.info("Erfolgreich mit Home Assistant verbunden!")
    except Exception as e:
        logger.error(f"Fehler beim Verbinden mit Home Assistant: {e}")
        return

    # Hauptloop
    while True:
        try:
            logger.info("Add-on läuft... (Intervall: {} Sekunden)".format(args.interval))
            # Hier kommt später deine Logik hin!
            time.sleep(args.interval)
        except KeyboardInterrupt:
            logger.info("Add-on wird beendet...")
            break
        except Exception as e:
            logger.error(f"Fehler im Hauptloop: {e}")
            time.sleep(10)  # Warte 10 Sekunden bei Fehlern

if __name__ == "__main__":
    main()