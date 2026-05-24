#!/usr/bin/env python3
import argparse
import logging
import time
import os
import requests
import json

def get_ha_state(api_url, token, entity_id):
    """Holt den Zustand eines Entities über die REST-API von Home Assistant."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    url = f"{api_url}/api/states/{entity_id}"
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()["state"]
        else:
            return None
    except Exception as e:
        logging.error(f"Fehler beim Abrufen von {entity_id}: {e}")
        return None

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
    logger.info("Starte Lastmanagement-Add-on (minimale Version)...")

    # Home Assistant API-URL und Token
    token = os.getenv("SUPERVISOR_TOKEN")
    api_url = os.getenv("HASSIO_API")

    if not token or not api_url:
        logger.error("SUPERVISOR_TOKEN oder HASSIO_API nicht gesetzt!")
        return

    logger.info(f"Verbinde mit Home Assistant unter {api_url}...")

    # Hauptloop
    while True:
        try:
            # PV-Leistung und Verbrauch abrufen
            pv_power = get_ha_state(api_url, token, "sensor.inverter_input_power")
            current_consumption = get_ha_state(api_url, token, "sensor.current_consumption")

            # Überschuss berechnen
            if pv_power is not None and current_consumption is not None:
                pv = float(pv_power)
                consumption = float(current_consumption)
                surplus = pv - consumption
                logger.info(f"PV-Leistung: {pv} W | Verbrauch: {consumption} W | Überschuss: {surplus} W")
            else:
                logger.warning("PV-Leistung oder Verbrauch nicht verfügbar")

            time.sleep(args.interval)

        except KeyboardInterrupt:
            logger.info("Add-on wird beendet...")
            break
        except Exception as e:
            logger.error(f"Fehler im Hauptloop: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()