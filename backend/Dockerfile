# Use a specific stable Python version
FROM python:3.11.9-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (for better Docker layer caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Ensure environment variables exist (optional: only if .env needed at runtime)
# COPY .env /app/.env

# Expose port (Render will map it automatically)
EXPOSE 5000

# Start FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
