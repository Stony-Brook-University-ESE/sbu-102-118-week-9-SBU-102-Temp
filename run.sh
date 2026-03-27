#!/bin/bash

# Motivational Video Generator Runner
echo "Cleaning up Docker containers and cache..."
docker system prune -f > /dev/null 2>&1

echo "Building Docker image..."
docker build -t motivational-video-generator .

# Check if API key is already set in environment
if [ -z "$GEMINI_API_KEY" ]; then
    echo ""
    echo "Please enter your Google Gemini API key:"
    echo "(Note: Your input will be visible - make sure no one is watching)"
    read -p "API Key: " GEMINI_API_KEY
    echo ""
else
    echo "Using existing API key from environment."
fi

# Validate API key is not empty
if [ -z "$GEMINI_API_KEY" ]; then
    echo "Error: No API key provided. Exiting."
    exit 1
fi

echo "Running Motivational Video Generator..."
docker run --rm -i \
  -v "$(pwd):/app" \
  -e GEMINI_API_KEY="$GEMINI_API_KEY" \
  motivational-video-generator

# Clean up after execution
echo ""
echo "Cleaning up Docker resources..."
docker rmi motivational-video-generator > /dev/null 2>&1
docker system prune -f > /dev/null 2>&1
echo "Cleanup complete!"