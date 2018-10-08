#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch as es
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler

c = CountVectorizer()

config = {'index': 'dataset',
              'doc_type': 'data'}

es = es()
data = es.search(index=config['index'], body={"query": {"match_all": {}}, "size": 1000})
hits = data['hits']['hits']

print "ilosc: ", len(hits)

corpus = []

for hit in hits:
    attrs = hit['_source']['properties']
    att_str = " ".join(attrs)
    corpus.append(att_str)

x = c.fit_transform(corpus)
print x.toarray()


