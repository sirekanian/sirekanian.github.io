#!/usr/bin/env bash

set -e

if [ $# -ne 0 ]; then
  wget -qO- "https://raw.githubusercontent.com/sirekanian/list-of-war-enablers/master/list-of-war-enablers.json" \
    >warmongr/list-of-war-enablers.json
  wget -qO- "https://raw.githubusercontent.com/sirekanian/list-of-war-enablers/master/input/data-en.txt" \
    >warmongr/list-of-war-enablers-primary.txt
  wget -qO- "https://raw.githubusercontent.com/sirekanian/list-of-war-enablers/master/input/data-ru.txt" \
    >warmongr/list-of-war-enablers-secondary.txt
fi

sh -c 'cd warmongr && ./update.py'
sh -c 'cd warmongr && ./localize.py'
sh -c 'cd warmongr && ./verify.py'
sh -c 'cd warmongr && ./index.py'
