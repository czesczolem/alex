#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import elasticsearch



def get_html_from_folder(path):
    files = os.listdir(path)
    pdf_files = [x for x in files if ".html" in x]
    return pdf_files

if __name__ == "__main__":

    config = {'index': 'ustawy_nlp',
              'doc_type': 'data'}

    es = elasticsearch.Elasticsearch()

    path = os.getcwd() + "/pdftxt/htmls/"
    htmls = get_html_from_folder(path)

    for num, x in enumerate(htmls):
        with open(path + x, 'r') as f:
            content = f.read()
        print num, ": saving to db"
        id = x.split(".")[0]
        # write_to_database(content, config, es, id)
        es.index(index=config['index'], doc_type=config['doc_type'], id=id, body={
            "properties": content
        })
    print htmls

