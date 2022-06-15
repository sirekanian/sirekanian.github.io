#!/usr/bin/env bash

set -e

wget -qO- "https://raw.githubusercontent.com/sirekanian/list-of-war-enablers/master/list-of-war-enablers.json" \
  >warmongr/list-of-war-enablers.json

wget -qO- "https://raw.githubusercontent.com/sirekanian/list-of-war-enablers/master/input/data.txt" \
  >warmongr/list-of-war-enablers.txt

echo "{\"date\":\"$(date -I)\"}" \
  >warmongr/meta.json
