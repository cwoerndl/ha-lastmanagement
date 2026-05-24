#!/usr/bin/with-contenv bashio
echo "Starte Lastmanagement-Add-on..."

CONFIG_PATH=/data/options.json
LOG_LEVEL=$(bashio::config 'log_level')
UPDATE_INTERVAL=$(bashio::config 'update_interval')

exec python3 /app/lastmanagement.py --config "$CONFIG_PATH" --log-level "$LOG_LEVEL" --interval "$UPDATE_INTERVAL"