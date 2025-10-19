#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset

echo "🚀 Starting deployment sequence..."

# ======================================================
# STEP 1: Ensure DB Tables Exist
# ======================================================
echo "📦 Checking PostgreSQL and creating tables if needed..."
python -c "from app.db.postgres import create_tables; create_tables()"

# ======================================================
# STEP 2: Start Celery Worker (in background)
# ======================================================
echo "⚙️ Launching Celery worker..."
celery -A worker worker --loglevel=info &

# ======================================================
# STEP 3: Launch FastAPI Web Server
# ======================================================
echo "🌐 Starting FastAPI server on port 8000..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
