FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.4
RUN elasticsearch-plugin remove x-pack
RUN elasticsearch-plugin install pl.allegro.tech.elasticsearch.plugin:elasticsearch-analysis-morfologik:5.6.4