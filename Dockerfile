# ------------ Build stage with Python + Django ------------
FROM python:3.12-slim as backend

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all Django project files (from root)
COPY . .

# ------------ Final image with Nginx ------------
#FROM debian:bullseye-slim
FROM python:3.12-slim
# Install Nginx and dependencies
RUN apt-get update && \
    apt-get install -y nginx curl && \
    rm /etc/nginx/sites-enabled/default && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy app from build stage
COPY --from=backend /app /app

# Copy nginx and entrypoint
COPY nginx.conf /etc/nginx/sites-enabled/default
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

WORKDIR /app
EXPOSE 80

CMD ["/app/entrypoint.sh"]
