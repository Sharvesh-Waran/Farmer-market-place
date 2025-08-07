#!/bin/bash
set -e  # fail if any command fails

cd /app/backend

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Django application..."
python manage.py runserver 0.0.0.0:8000 &

echo "Starting Nginx..."
exec nginx -g "daemon off;"
