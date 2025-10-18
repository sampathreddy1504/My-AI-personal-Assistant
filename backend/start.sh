#!/bin/bash
# ===============================================
# 🚀 Start Script for Personal AI Assistant Backend
# Runs FastAPI API + Celery Worker + Celery Beat
# ===============================================

echo "🔧 Initializing environment..."

# Exit immediately if a command exits with a non-zero status
set -e

# Display environment info
echo "🐍 Python version: $(python --version)"
echo "📦 Installed packages:"
pip list | grep -E "fastapi|uvicorn|celery|redis|psycopg2" || true

echo "🚀 Starting Personal AI Assistant backend services..."

# Start Celery worker (background)
echo "⚙️ Starting Celery worker..."
celery -A app.worker.celery worker --loglevel=info &

# Start Celery beat scheduler (background, runs periodic tasks)
echo "⏰ Starting Celery beat..."
celery -A app.worker.celery beat --loglevel=info &

# Start FastAPI app via Uvicorn
echo "🌐 Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
