# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 00:50:08 2018

@author: kyjna
"""

import requests
import json

json_url = 'https://askdjango.github.io/lv2/data.json'

json_string = requests.get(json_url).text

data_list = json.loads(json_string)

for data in data_list:
    print(data['name'], data['url'])