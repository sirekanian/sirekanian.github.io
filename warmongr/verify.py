#!/usr/bin/env python3

import json


class TagSet:
    def __init__(self):
        self.__tags = dict()

    def put(self, name, count):
        if name in self.__tags:
            raise Exception('Tag name is not unique: ' + name)
        self.__tags[name] = count

    def compare(self, other):
        t1 = self.__tags
        t2 = other.__tags
        for x, y in t1.items():
            if x not in t2:
                print(f'{y}\t{"-"}\t{x}')
        for x, y in t2.items():
            if x not in t1:
                print(f'{"-"}\t{y}\t{x}')
        for x, y1 in t1.items():
            if x in t2:
                y2 = t2[x]
                if abs(y1 - y2) > 2:
                    print(f'{y1}\t{y2}\t{x}')


def main(filename):
    tags1 = TagSet()
    j = json.load(open(filename))
    lang = j['locale']
    for group in j['props']['pageProps']['villainsList']:
        if group['name'] in {'Full sanctions list', 'List updates'}:
            continue
        if group['name'] in {'Полный санкционный список', 'Обновления списка'}:
            continue
        count = 0
        for doc in group['lists']:
            count += doc['number']
        tags1.put(group['name'], count)
    tags2 = TagSet()
    for t in json.load(open('tags.json')):
        tags2.put(t[lang + 'Name'], t['count'])
    tags1.compare(tags2)


main('list-of-war-enablers-primary.txt')
main('list-of-war-enablers-secondary.txt')
