#!/usr/bin/with-contenv bashio
echo "Starte Lastmanagement-Add-on..."

# Lade Konfiguration
CONFIG_PATH=/data/options.json
LOG_LEVEL=$(bashio::config 'log_level')
UPDATE_INTERVAL=$(bashio::config 'update_interval')

# Starte das Python-Skript
python3 /app/lastmanagement.py --config /data/options.json --log-level $LOG_LEVEL --interval $UPDATE_INTERVAL