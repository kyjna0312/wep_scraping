# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:28:13 2018

@author: kyjna
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://askdjango.github.io/lv1/')

html = response.text

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('p'):
    print(tag.text)