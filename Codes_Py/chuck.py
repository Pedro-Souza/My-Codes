#!/usr/bin/env python
# coding: utf-8


from requests import get
from json import loads


req = get("http://api.icndb.com/jokes/random/").text
req = loads(req)
print(req['value']['joke'])
