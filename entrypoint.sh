#!/bin/bash
set -e
cd /app

echo "Starting Django app..."

python3 manage.py runserver 0.0.0.0:8000

echo "Starting Nginx..."
exec nginx -g "daemon off;"
