#!/bin/bash
set -a
source .env
set +a

# Substitute env vars into a temp config
envsubst < ./config/odoo.conf > /tmp/odoo.conf

# Run Odoo with resolved config
exec python3 odoo-bin -c /tmp/odoo.conf "$@"
