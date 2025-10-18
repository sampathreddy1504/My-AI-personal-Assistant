#!/bin/bash
set -e

echo "🔧 Initializing environment..."
python --version

echo "🔄 Uninstall any old psycopg remnants (if any)..."
pip uninstall -y psycopg2 psycopg2-binary || true
pip install -U psycopg[binary]==3.2.1

echo "🚀 Starting Personal AI Assistant backend services..."

# Start Celery worker and beat in background
celery -A app.worker.celery worker --loglevel=info &
celery -A app.worker.celery beat --loglevel=info &

# Start FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000
