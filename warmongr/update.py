#!/usr/bin/env python3
import json
import re


def normalize(name):
    name = re.sub(r'\.$', '', name)
    name = re.sub(r'["“”]', '', name)
    name = re.sub(r', etc$', '', name)
    name = re.sub(r'^Sellout celebrities$', 'Celebrities, influencers and bloggers', name)
    name = re.sub(r'^Influencers and bloggers$', 'Celebrities, influencers and bloggers', name)
    name = re.sub(r'^United Russia party', '‘United Russia’ party', name)
    name = re.sub(r'^Federal media employees$', 'Federal media', name)
    return name


class Tags:
    def __init__(self):
        self.tags_by_name = dict()
        self.groups = set()
        for group in json.load(open('list-of-war-enablers.txt'))['props']['pageProps']['villainsListEN']:
            if group['name'] not in {'Full sanctions list', 'List updates'}:
                self.groups.add(group['name'])

    def add(self, name):
        name = normalize(name)
        if name in self.groups:
            return
        if name in self.tags_by_name:
            self.tags_by_name[name].inc()
        else:
            id = len(self.tags_by_name) + 1
            self.tags_by_name[name] = Tag(id, name)

    def json(self):
        j = [t.json() for t in self.tags_by_name.values()]
        j = sorted(j, key=lambda x: x['count'], reverse=True)
        return j

    def names_to_ids(self, names):
        ids = set()
        for name in names:
            name = normalize(name)
            if name in self.groups:
                continue
            ids.add(self.tags_by_name[name].id)
        return sorted(ids)


class Tag:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.count = 1

    def inc(self):
        self.count += 1

    def json(self):
        return {'id': self.id, 'name': self.name, 'count': self.count}


if __name__ == '__main__':
    data = list()
    tags = Tags()
    for row in json.load(open('list-of-war-enablers.json')):
        for tag in row['5']:
            tags.add(tag)
        row['5'] = tags.names_to_ids(row['5'])
        data += [row]
    json.dump(data, open('data.json', 'w'), ensure_ascii=False, indent=2)
    json.dump(tags.json(), open('tags.json', 'w'), ensure_ascii=False, indent=2)
