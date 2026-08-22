#!/bin/bash
set -e

echo "Running migrations..."
alembic upgrade head

echo "Seeding roles..."
python -m app.scripts.seed_roles

echo "Starting server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
