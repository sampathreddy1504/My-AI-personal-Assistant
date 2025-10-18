#!/bin/bash
# ===============================================
# 🚀 Upgraded Start Script for Personal AI Assistant
# Ensures correct environment and dependencies
# ===============================================

echo "🔧 Initializing environment..."

# Exit immediately if a command fails
set -e

# Set default PORT if not defined
export PORT=${PORT:-8000}

# Create virtual environment if not exists
if [ ! -d ".venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies from requirements.txt
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Show environment info
echo "🐍 Python version: $(python --version)"
echo "📦 Installed packages: "
pip list | grep -E "fastapi|uvicorn|celery|redis|psycopg|neo4j|cohere|pydantic|sqlalchemy" || true

# Start Celery worker (background)
echo "⚙️ Starting Celery worker..."
celery -A app.worker.celery worker --loglevel=info &

# Start Celery beat scheduler (background)
echo "⏰ Starting Celery beat..."
celery -A app.worker.celery beat --loglevel=info &

# Start FastAPI via Uvicorn
echo "🌐 Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
