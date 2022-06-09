#!/usr/bin/env bash

set -e

wget -qO- "https://raw.githubusercontent.com/sirekanian/list-of-war-enablers/master/list-of-war-enablers.json" \
  > warmongr/data.json

echo "{\"date\":\"$(date -I)\"}" \
  > warmongr/meta.json
