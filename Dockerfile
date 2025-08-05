# Backend build stage
FROM python:3.12-slim as backend

WORKDIR /app

# Copy entire project (since everything is at root level)
COPY . /app/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Final image stage
FROM debian:bullseye-slim

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    rm /etc/nginx/sites-enabled/default && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy backend and templates
COPY --from=backend /app /app

# Copy frontend HTML to nginx (optional, in case you want to serve static pages via Nginx)
# If you’re using Django templating only, you might skip this
COPY --from=backend /app/templates /var/www/html

# Copy entrypoint and nginx config
COPY entrypoint.sh /app/entrypoint.sh
COPY nginx.conf /etc/nginx/sites-enabled/default
RUN chmod +x /app/entrypoint.sh

# Set working directory and expose port
WORKDIR /app
EXPOSE 80

# Run entrypoint
CMD ["/app/entrypoint.sh"]
