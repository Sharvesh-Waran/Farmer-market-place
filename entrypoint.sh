#!/bin/bash
#set -e

#cd /app

#echo "Running Django migrations..."
#python3 manage.py migrate

#echo "Collecting static files..."
#python3 manage.py collectstatic --settings=market.settings --noinput
#python3 manage.py shell
# Set default OTLP endpoint if not provided
#OTEL_EXPORTER_OTLP_ENDPOINT=${OTEL_EXPORTER_OTLP_ENDPOINT:-http://otel-collector-opentelemetry-collector.mointorlgpt.svc.cluster.local:4318}

#echo "Starting Django with OpenTelemetry (Gunicorn)..."
#opentelemetry-instrument \
 # --traces_exporter otlp \
  #--exporter_otlp_endpoint $OTEL_EXPORTER_OTLP_ENDPOINT \
  #gunicorn market.wsgi:application --bind 0.0.0.0:8000

#echo "Starting Nginx..."
#exec nginx -g "daemon off;"
#!/bin/bash
set -e

cd /app

echo "Collecting static files..."
opentelemetry-instrument \
  --traces_exporter otlp \
  --exporter_otlp_endpoint http://otel-collector-opentelemetry-collector.mointorlgpt.svc.cluster.local:4318 \
  python manage.py collectstatic --noinput

echo "Starting Django with OpenTelemetry (Gunicorn)..."
exec opentelemetry-instrument \
  --traces_exporter otlp \
  --exporter_otlp_endpoint http://otel-collector-opentelemetry-collector.mointorlgpt.svc.cluster.local:4318 \
  gunicorn market.wsgi:application --bind 0.0.0.0:8000

echo "Starting Nginx..."
exec nginx -g "daemon off;"
