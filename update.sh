#!/usr/bin/env bash

set -e

wget -qO- "https://raw.githubusercontent.com/sirekanian/bribetakers/master/bribetakers.json" \
  > warmongr/data.json

echo "{\"date\":\"$(date -I)\"}" \
  > warmongr/meta.json
