#!/bin/bash

VERSION=$(cat VERSION)

docker build . -t ghcr.io/fredoaf/traffic-display:$VERSION
docker push ghcr.io/fredoaf/traffic-display:$VERSION

API_KEY="null"

docker run --rm -it --network host \
  -e DATA_DIR='./' ghcr.io/fredoaf/traffic-display:$VERSION