x
#!/bin/bash

echo "🧹 Starting Docker cleanup..."

# Stop all running containers
echo "⏹️ Stopping running containers..."
docker stop $(docker ps -q) 2>/dev/null

# Remove all containers
echo "🗑️ Removing all containers..."
docker rm -f $(docker ps -aq) 2>/dev/null

# Remove all images
echo "🧱 Removing all images..."
docker rmi -f $(docker images -aq) 2>/dev/null

# Remove all volumes
echo "💾 Removing all volumes..."
docker volume rm $(docker volume ls -q) 2>/dev/null

# Remove all unused networks
echo "🌐 Removing unused networks..."
docker network prune -f 2>/dev/null

# Remove all build cache and dangling data
echo "🚮 Pruning system..."
docker system prune -a --volumes -f 2>/dev/null

echo "✅ Docker cleanup complete!"
