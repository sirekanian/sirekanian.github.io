#!/usr/bin/env python3
import json
import re


def capitalize(name):
    if re.match(r'^[A-Za-zА-Яа-яЁё ]+$', name):
        parts = name.split()
        if len(parts) == 3:
            return ' '.join([x.capitalize() for x in parts])
    return name


def normalize(name):
    name = re.sub(r'\.$', '', name)
    name = re.sub(r'["“”]', '', name)
    name = re.sub(r', etc$', '', name)
    name = re.sub(r'^Sellout celebrities$', 'Celebrities, influencers and bloggers', name)
    name = re.sub(r'^Influencers and bloggers$', 'Celebrities, influencers and bloggers', name)
    name = re.sub(r'^United Russia party', '‘United Russia’ party', name)
    name = re.sub(r'^Federal media employees$', 'Federal media', name)
    return name


class Normalizer:
    def __init__(self):
        self.groups = set()
        self.ungroups = dict()
        for group in json.load(open('list-of-war-enablers-primary.txt'))['props']['pageProps']['villainsList']:
            if group['name'] not in {'Full sanctions list', 'List updates'}:
                self.groups.add(group['name'])
                for tag in group['lists']:
                    self.ungroups[tag['name']] = group['name']

    def normalize(self, names):
        normalized = set()
        for name in names:
            name = normalize(name)
            if name in self.ungroups:
                name = self.ungroups[name]
            if name in self.groups:
                normalized.add(name)
        return sorted(normalized)


class Tags:
    def __init__(self):
        self.tags_by_name = dict()
        self.tags_frequency = dict()
        self.normalizer = Normalizer()

    def add(self, names):
        for name in self.normalizer.normalize(names):
            if name in self.tags_by_name:
                self.tags_frequency[name] += 1
            else:
                self.tags_frequency[name] = 1
        for i, (x, y) in enumerate(sorted(self.tags_frequency.items(), key=lambda x: -x[1])):
            self.tags_by_name[x] = Tag(i + 1, x, y)

    def json(self):
        j = [t.json() for t in self.tags_by_name.values()]
        j = sorted(j, key=lambda x: x['count'], reverse=True)
        return j

    def names_to_ids(self, names):
        ids = set()
        for name in self.normalizer.normalize(names):
            ids.add(self.tags_by_name[name].id)
        return sorted(ids)


class Tag:
    def __init__(self, id, name, count):
        self.id = id
        self.name = name
        self.count = count

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'shortName': '',
            'ruName': '',
            'ruShortName': '',
            'count': self.count,
        }


def main():
    data = json.load(open('list-of-war-enablers.json'))
    tags = Tags()
    for row in data:
        tags.add(row['5'])
    for row in data:
        row['0'] = capitalize(row['0'])
        row['1'] = capitalize(row['1'])
        row['5'] = tags.names_to_ids(row['5'])
    json.dump(data, open('data.json', 'w'), ensure_ascii=False, indent=2)
    json.dump(tags.json(), open('tags.json', 'w'), ensure_ascii=False, indent=2)


main()
