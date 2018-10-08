
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch as es
from bs4 import BeautifulSoup as bs
from helpers import get_html_from_folder
import os

tag = 'span'
config = {'index': 'dataset',
              'doc_type': 'data'}



if __name__ == "__main__":

    es = es()
    path = os.getcwd() + "/pdftxt/htmls/"
    htmls = get_html_from_folder(path)
    id = 0
    for html in htmls:
        with open(path + html, 'r') as f:
            data = f.read().strip()

        soup = bs(data, 'lxml')
        tags = soup.findAll(tag)

        for n, t in enumerate(tags):
            tag_style = t.attrs['style']
            tag_style = tag_style.split()
            doc_id = str(id)
            print "id: ", id, "html: ", html, "style: ", tag
            es.index(index=config['index'], doc_type=config['doc_type'], id=doc_id, body={
                "properties": tag_style
            })
            id += 1
