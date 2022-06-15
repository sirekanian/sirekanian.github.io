#!/usr/bin/env bash

set -e

if [ $# -ne 0 ]; then
  wget -qO- "https://raw.githubusercontent.com/sirekanian/list-of-war-enablers/master/list-of-war-enablers.json" \
    >warmongr/list-of-war-enablers.json
  wget -qO- "https://raw.githubusercontent.com/sirekanian/list-of-war-enablers/master/input/data.txt" \
    >warmongr/list-of-war-enablers.txt
fi

sh -c 'cd warmongr && ./update.py'
sh -c 'cd warmongr && ./verify.py'
sh -c 'cd warmongr && ./index.py'

if [ $# -ne 0 ]; then
  echo "{\"date\":\"$(date -I)\"}" \
    >warmongr/meta.json
fi
