#!/bin/bash
set -a
source .env
set +a

# Substitute env vars into a temp config
envsubst < ./config/odoo.conf > /tmp/odoo.conf


# Check if the database exists in Postgres
DB_EXISTS=$(psql -h "$DB_HOST" -U "$DB_USER" -tAc "SELECT 1 FROM pg_database WHERE datname='${DB_NAME}';")

if [ "$DB_EXISTS" != "1" ]; then
  echo "Database ${DB_NAME} does not exist. Initializing..."
  python3 odoo-bin -c /tmp/odoo.conf -d "$DB_NAME" --without-demo=all -i base --stop-after-init
fi


# Run Odoo with resolved config
exec python3 odoo-bin -c /tmp/odoo.conf "$@"
