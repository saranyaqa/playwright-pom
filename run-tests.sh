#!/bin/bash

# Ensure the script exits on any error
set -e

echo "🚀 Running Playwright tests in Docker..."

# Build the Docker image if it doesn't exist
docker-compose build --pull

# Run tests in the container
docker-compose run --rm playwright
