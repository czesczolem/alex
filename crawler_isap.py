import shutil
import requests
import time
import random

url = 'http://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20180001676/O/D20181676.pdf'

def download_from_url(url, filename):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    response = requests.get(url, stream=True, headers=headers)
    if response:
        print filename, " Downloaded"
        with open('pdfs/' + filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

def extend_number_string(number):
    while len(number) < 4:
        number = "0" + number
    return number
# pdf2txt pdf2txt.py ustawa.pdf

for x in range(1805,4000):
    time.sleep(random.randint(5, 30))
    print "sleeping, x = ",x
    number = extend_number_string(str(x))
    url_gen = "http://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU2018000{}/O/D2018{}.pdf".format(number, number)
    download_from_url(url_gen, number + ".pdf")
