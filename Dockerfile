# ------------ Build stage ------------
FROM python:3.12-slim as backend

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire Django project
COPY . .

# ------------ Final image with Nginx and Python ------------
FROM python:3.12-slim

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx curl && \
    rm /etc/nginx/sites-enabled/default && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy from builder stage
COPY --from=backend /app /app

# Optional: install Python dependencies again (safe redundancy)
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy Nginx and entrypoint
COPY nginx.conf /etc/nginx/sites-enabled/default
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 80

CMD ["/app/entrypoint.sh"]
