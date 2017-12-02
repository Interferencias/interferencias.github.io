#!/usr/bin/env python
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

'''
Dependencies:
    PyYAML ^3.12
'''

import yaml
import urllib2
import json

token = open("access_token","r").read()
authors = {}
avatars = {}

with open("authors.yml", "r") as f:
    authors = yaml.load(f)

    for key in authors:
        user = json.loads(urllib2.urlopen("https://api.github.com/users/" + key + "?access_token=" + token).read())
        avatars[key] = user["avatar_url"]

for key, value in avatars.items():
    authors[key]["avatar"] = value

with open('authors.yml', 'w') as f:
    yaml.safe_dump(authors, f, default_flow_style = False, allow_unicode = True)
