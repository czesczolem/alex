from elasticsearch import Elasticsearch as es
from bs4 import BeautifulSoup as bs


path = 'pdftxt/htmls/'
file = '0012.html'

with open(path + file, 'r') as f:
    data = f.read().strip()

soup = bs(data, 'lxml')

spans = soup.findAll('span')

span = spans[0]

print 'allah akbar'

