#!/bin/bash

# Run Django migrations and start the server
cd /app/backend
python manage.py migrate
python manage.py collectstatic --noinput &
python manage.py runserver 0.0.0.0:8000 &

# Start nginx
nginx -g "daemon off;"
