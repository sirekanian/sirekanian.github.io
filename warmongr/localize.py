#!/usr/bin/env python3
import json

localization = dict()
en_groups = json.load(open('list-of-war-enablers-en.txt'))['props']['pageProps']['villainsList']
ru_groups = json.load(open('list-of-war-enablers-ru.txt'))['props']['pageProps']['villainsList']
if len(en_groups) != len(ru_groups):
    raise Exception('group count not matches')
group_count = len(en_groups)
for i in range(0, group_count):
    localization[en_groups[i]['name']] = ru_groups[i]['name']
    en_lists = en_groups[i]['lists']
    ru_lists = ru_groups[i]['lists']
    if len(en_lists) != len(ru_lists):
        raise Exception('lists count not matches for ' + en_groups['name'])
    lists_count = len(en_lists)
    for j in range(0, lists_count):
        localization[en_lists[j]['name']] = ru_lists[j]['name']

short_names = json.load(open('shortened.json'))

tags = json.load(open('tags.json'))
for tag in tags:
    tag['ruName'] = localization[tag['name']]
    if tag['name'] not in short_names or not short_names[tag['name']]:
        print('WARN: Short name not found: ' + tag['name'])
        short_names[tag['name']] = tag['name']
    if tag['ruName'] not in short_names or not short_names[tag['ruName']]:
        print('WARN: Short name not found: ' + tag['ruName'])
        short_names[tag['ruName']] = tag['ruName']
    tag['shortName'] = short_names[tag['name']]
    tag['ruShortName'] = short_names[tag['ruName']]
json.dump(tags, open('tags.json', 'w'), ensure_ascii=False, indent=2)
