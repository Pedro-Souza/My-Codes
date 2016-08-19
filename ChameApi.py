#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from requests import get
from json import loads

b = []
req = loads(get(
    "https://chameleonbit.trade/api/v1/get_coin_data.php?id_coin=2").text)
for i in req:
    for a in req[i]:
        b = a
print(b['buy'])

# In construction...
