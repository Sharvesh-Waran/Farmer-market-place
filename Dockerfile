# ------------ Backend build stage ------------
FROM python:3.12-slim as backend

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy backend code
COPY backend/ ./backend/

# ------------ Final image stage with Nginx ------------
FROM debian:bullseye-slim

# Install Nginx and dependencies
RUN apt-get update && \
    apt-get install -y nginx curl && \
    rm /etc/nginx/sites-enabled/default && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy backend app from previous stage
COPY --from=backend /app /app

# Copy nginx config and entrypoint
COPY nginx.conf /etc/nginx/sites-enabled/default
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

WORKDIR /app
EXPOSE 80

CMD ["/app/entrypoint.sh"]
