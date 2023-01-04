#!/usr/bin/env python3
import json

localization = dict()
json1 = json.load(open('list-of-war-enablers-primary.txt'))
json2 = json.load(open('list-of-war-enablers-secondary.txt'))
groups1 = json1['props']['pageProps']['villainsList']
groups2 = json2['props']['pageProps']['villainsList']
if len(groups1) != len(groups2):
    raise Exception('group count not matches')
group_count = len(groups1)
for i in range(0, group_count):
    localization[groups1[i]['name']] = groups2[i]['name']
    lists1 = groups1[i]['lists']
    lists2 = groups2[i]['lists']
    if len(lists1) != len(lists2):
        raise Exception('lists count not matches for ' + groups1['name'])
    lists_count = len(lists1)
    for j in range(0, lists_count):
        localization[lists1[j]['name']] = lists2[j]['name']

short_names = json.load(open('shortened.json'))

tags = json.load(open('tags.json'))
localizedTags = list()
lang1 = json1['locale']
lang2 = json2['locale']
for tag in tags:
    name1 = tag['name']
    name2 = localization[tag['name']]
    if name1 not in short_names or not short_names[name1]:
        print('ERROR: Short name not found: ' + name1)
        exit(1)
    if name2 not in short_names or not short_names[name2]:
        print('ERROR: Short name not found: ' + name2)
        exit(1)
    localizedTags += [{
        'id': tag['id'],
        lang1 + 'Name': name1,
        lang1 + 'ShortName': short_names[name1],
        lang2 + 'Name': name2,
        lang2 + 'ShortName': short_names[name2],
        'count': tag['count'],
    }]
if len(localizedTags) == 0:
    raise Exception('empty localized tags, something went wrong')
else:
    json.dump(localizedTags, open('tags.json', 'w'), ensure_ascii=False, indent=2)
