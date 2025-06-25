#!/bin/bash
# Launch Label Studio in Docker, always removing any previous container with the same name

# Usage: ./scripts/run_label_studio.sh

docker rm -f label-studio-dev 2>/dev/null

docker run --rm -it \
  --name label-studio-dev \
  -p 8080:8080 \
  -v "$(dirname "$0")/../mydata:/label-studio/data" \
  heartexlabs/label-studio@sha256:60fd8002d80050956509a8bdcf2ce2f487cccd7647161fc6527265983a066b03
