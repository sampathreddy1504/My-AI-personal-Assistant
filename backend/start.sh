#!/bin/bash
set -e

# Upgrade pip to avoid old resolver issues
pip install --upgrade pip

# Install requirements fresh
pip install --no-cache-dir -r requirements.txt

# Start Celery and FastAPI
celery -A app.worker.celery beat --detach
celery -A app.worker.celery worker --detach
uvicorn app.main:app --host 0.0.0.0 --port $PORT
