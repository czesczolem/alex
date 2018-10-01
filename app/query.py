#!/usr/bin/python
# -*- coding: utf-8 -*-

import elasticsearch


def preprocessing(data):
    data = data.replace('\n', '<br>')
    return data


if __name__ == "__main__":
    es = elasticsearch.Elasticsearch([{'host': '0.0.0.0', 'port': 9200}])
    res = es.search(index="ustawy", body={"query": {"match": {"content": 'instytucję kredytową'}}})
    data =  res['hits']['hits'][0]['_source']['content']
    prep_data = preprocessing(data)
    print "elo"