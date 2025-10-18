#!/bin/bash

# Activate virtual environment
source /opt/render/project/src/.venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run Celery worker (adjust path if needed)
celery -A app.worker.celery worker --loglevel=info &

# Run FastAPI app
uvicorn app.main:app --host 0.0.0.0 --port $PORT
