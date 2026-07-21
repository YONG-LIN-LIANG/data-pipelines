#!/bin/bash

# Ensure the script stops immediately if any error occurs to prevent unintended consequences
set -e

echo "🚀 Starting complete environment reset..."

# 1. Stop and remove all containers, networks, and Docker volumes
echo "🛑 Shutting down and clearing Docker containers and volumes..."
docker-compose down -v

# 2. Completely delete the local mounted postgres data directory to ensure init scripts re-trigger
echo "🗑️ Deleting local Postgres physical data directory..."
if [ -d "./postgres/data" ]; then
    rm -rf ./postgres/data
    echo "✅ Successfully cleared ./postgres/data"
else
    echo "ℹ️ No local ./postgres/data directory found, skipping deletion"
fi

# 3. Restart all services and stream logs directly to the terminal
echo "✨ Restarting all services and initializing (please monitor the terminal screen)..."
docker-compose up