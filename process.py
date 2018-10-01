#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

def pdf_to_html(pdf_path):
    content = subprocess.check_output(['pdf2txt.py', '-t', 'html', pdf_path])
    return content

def pdf_to_txt(pdf_path):
    content = subprocess.check_output(['pdf2txt.py', pdf_path])
    return content

def get_pdfs_from_folder(path):
    files = os.listdir(path)
    pdf_files = [x for x in files if ".pdf" in x]
    return pdf_files


if __name__ == "__main__":

    if sys.argv[1]:
        path = sys.argv[1]
    else:
        path = "pdfs/"
    pdfs = get_pdfs_from_folder(path + '/pdfs/')
    if not pdfs:
        print "no pdfs"
    else:
        for x in pdfs:
            print "parsing pdf: ", x
            try:
                html = pdf_to_html(path + '/pdfs/' + x)
            except:
                print "parsing error"
            id = x.split(".")[0]
            print "saving: ", x
            with open(path + '/htmls/' + id + ".html", "w") as f:
                f.write(html)

