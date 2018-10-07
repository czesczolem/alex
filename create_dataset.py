
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch as es
from bs4 import BeautifulSoup as bs
path = 'pdftxt/htmls/'
file = '0012.html'
tag = 'span'

config = {'index': 'dataset',
              'doc_type': 'data'}

es = es()

def process(x):
    x = x.split()
    return x

with open(path + file, 'r') as f:
    data = f.read().strip()

soup = bs(data, 'lxml')
tags = soup.findAll(tag)

for n, t in enumerate(tags):
    tag_style = t.attrs['style']
    tag_style = tag_style.split()
    id = str(n)
    es.index(index=config['index'], doc_type=config['doc_type'], id=id, body={
        "properties": tag_style
    })
