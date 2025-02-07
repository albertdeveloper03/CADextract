# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app
ENV APP_PATH=/app
ENV DB_PARAMS=localhost
ENV FLASK_ENV=development
ENV MPLBACKEND=Agg

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    poppler-utils \
    python3-dev \
    build-essential \
    libcairo2-dev \
    pkg-config \
    python3-tk \
    libfreetype6-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create and set permissions for temporary directory
RUN mkdir -p /app/temporary && chmod 777 /app/temporary

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--chdir", "/app", "views:app"]