#!/bin/bash
set -e

cd /app

#echo "Running Django migrations..."
#python3 manage.py migrate

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Starting Django..."
python3 manage.py runserver 0.0.0.0:8000 &

echo "starting Nginx..."
exec nginx -g "daemon off;"
