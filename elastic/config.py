#!/usr/bin/env python

from elasticsearch import Elasticsearch

html_ignore_settings = {
    "settings": {
        "analysis": {
            "analyzer": {
                "nlp": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "char_filter": [
                        "html_strip"
                    ],
                    "filter": [
                        "standard",
                        "lowercase",
                        "morfologik_stem"
                    ]
                }
            }
        }
    }
}


def configure(es_client):
    index_name = "ustawy_nlp"
    document_type = "data"
    es_client.indices.create(index=index_name, body=html_ignore_settings)

    data_mapping = {
        document_type: {
            "properties": {
                "context": {
                    "type": "text",
                    "analyzer": "nlp"
                }
            }
        }
    }

    es_client.indices.put_mapping(index=index_name, doc_type=document_type, body=data_mapping)

if __name__ == "__main__":
    es = Elasticsearch()
    configure(es)

