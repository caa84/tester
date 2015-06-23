#!/usr/bin/env python

import os
import json

with open ("hook_payload.json", "r") as file:
    data = file.read().replace('\n', '')

parsed_json = json.loads( data )

ref = parsed_json['ref']
oldrev = parsed_json['before']
newrev = parsed_json['commits'][0]['id']
commit_message = parsed_json['commits'][0]['message']

vars = [ ref, oldrev, newrev, commit_message ]

print( vars )

