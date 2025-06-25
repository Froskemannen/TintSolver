#!/bin/bash
# Launch Label Studio in Docker, always removing any previous container with the same name

# Usage: ./scripts/run_label_studio.sh

docker rm -f label-studio-dev 2>/dev/null

docker run --rm -it \
  --name label-studio-dev \
  -p 8080:8080 \
  -v "$(pwd)/mydata:/label-studio/data" \
  heartexlabs/label-studio:latest
