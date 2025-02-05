# Dockerfile for ui-master
FROM python:3.9-slim

# Install system dependencies including pdftoppm
RUN apt-get update && apt-get install -y \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .
COPY ../DigiEDraw /app/DigiEDraw

# Create necessary directories
RUN mkdir -p /app/temporary

# Update paths in views.py
RUN sed -i 's|C:/Users/alalb/ui-master|/app|g' views.py && \
    sed -i 's|C:/Users/alalb/DigiEDraw/main.py|/app/DigiEDraw/main.py|g' views.py && \
    sed -i 's|localhost|redis|g' views.py

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "views:app"]