# Use official Python 3.11 slim image
FROM python:3.11-slim

# Install system dependencies required for psycopg/PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Copy .env file (if available)
COPY .env /app/.env

# Expose FastAPI port
EXPOSE 5000

# Command to run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
