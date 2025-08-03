# Backend build stage
FROM python:3.12-slim as backend

WORKDIR /app
COPY backend/ /app/backend/
COPY frontend/ /app/frontend/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r backend/requirements.txt

# Final image
FROM debian:bullseye-slim

# Install Nginx and required tools
RUN apt-get update && \
    apt-get install -y nginx && \
    rm /etc/nginx/sites-enabled/default && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy backend and frontend
COPY --from=backend /app/backend /app/backend
COPY --from=backend /app/frontend /var/www/html

# Copy entrypoint and config
COPY entrypoint.sh /app/entrypoint.sh
COPY nginx.conf /etc/nginx/sites-enabled/default
RUN chmod +x /app/entrypoint.sh

# Set working dir and expose port
WORKDIR /app
EXPOSE 80

# Run the app
CMD ["/app/entrypoint.sh"]
