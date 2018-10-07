#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch as es
from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()

config = {'index': 'dataset',
              'doc_type': 'data'}

es = es()
data = es.search(index=config['index'], body={"query": {"match_all": {}}, "size": 1000})
hits = data['hits']['hits']

print "ilosc: ", len(hits)

corpus = ''

for hit in hits:
    attrs = hit['_source']['properties']
    att_str = " ".join(attrs)
    corpus += att_str

X_train_counts = count_vect.fit_transform(corpus.split())
print X_train_counts.toarray().shape


