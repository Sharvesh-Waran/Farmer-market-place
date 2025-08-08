#!/bin/bash
set -e

cd /app

echo "Running Django migrations..."
python3 manage.py migrate

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Starting Django with OpenTelemetry..."
opentelemetry-instrument \
  --traces_exporter otlp \
  --exporter_otlp_endpoint http://otel-collector-opentelemetry-collector.mointorlgpt.svc.cluster.local:4318 \
  gunicorn market.wsgi:application --bind 0.0.0.0:8000

  #python manage.py runserver 0.0.0.0:8000

echo "Starting Nginx..."
exec nginx -g "daemon off;"
