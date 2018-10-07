#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, render_template, redirect, url_for
from flask import jsonify
import os
import elasticsearch
import query

app = Flask(__name__)

es = elasticsearch.Elasticsearch([{'host': '172.24.0.1', 'port': 9200}])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_html', methods=['GET', 'POST'])
def search_html():
    if request.method == 'POST':
        text = request.form['text']
        es_query = es.search(index='ustawy_nlp', body={"query": {"match": {"properties": text}}})
        if es_query['hits']['hits']:
            id = es_query['hits']['hits'][0]['_id']
            return redirect(url_for('search_html_id', id=id))
        else:
            return "no such query"
    else:
        return render_template('search.html')

@app.route('/search_html/<id>')
def search_html_id(id):
    if not id:
        return render_template('search.html')
    else:
        es_query = es.search(index='data1', body={"query": {"match": {"_id": id}}})
        if es_query['hits']['hits']:
            data = es_query['hits']['hits'][0]['_source']['content']
            return data
        else:
            return "dupa"

@app.route('/search_id', methods=['GET', 'POST'])
def search_id():
    if request.method == 'POST':
        es_query = es.search(index='data1', body={"query": {"match": {"_id": "1"}}})
        if es_query['hits']['hits']:
            data = es_query['hits']['hits'][0]['_source']['content']
            prep_data = query.preprocessing(data)
            return prep_data
        else:
            return "no such query"
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)