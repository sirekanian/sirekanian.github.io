#!/usr/bin/env python3
import itertools
import json


def join(value):
    return ' '.join(str(x) for x in sorted(value))


def calculate(data):
    index = dict()
    for tags in [set(row['5']) for row in data]:
        for permutation in itertools.permutations(tags, len(tags)):
            length = len(permutation)
            for position in range(1, length):
                key = join(permutation[0:position])
                value = set(permutation[position:length])
                if key in index:
                    index[key].update(value)
                else:
                    index[key] = value
    for key, value in index.items():
        index[key] = join(value)
    return index


def main():
    index = calculate(json.load(open('data.json')))
    json.dump(index, open('index.json', 'w'), ensure_ascii=False, indent=2)


main()
