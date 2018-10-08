import os

def get_html_from_folder(path):
    files = os.listdir(path)
    pdf_files = [x for x in files if ".html" in x]
    return pdf_files