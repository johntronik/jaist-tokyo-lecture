import requests
from bs4 import BeautifulSoup
from time import sleep
from typing import List


def get_jaist_lecture_pdf(year: int) -> List[str]:
    """save jaist lecture pdfs"""

    url_top = 'https://www.jaist.ac.jp/satellite/sate/lecture/'
    r = requests.get(url_top)
    soup = BeautifulSoup(r.content, features="lxml")
    # get links
    pdf_links = [l for l in soup.find_all(
        'dl') if '知識・情報科学系共通：月別時間割' in l.get_text()]
    pdf_links = [[a['href'] for a in l.find_all(
        'a') if str(year) in a['href']] for l in pdf_links]
    # flatten list
    pdf_links = sum(pdf_links, [])

    # save pdfs
    file_names = []
    for pdf_link in pdf_links:
        file_name = 'pdfs/'+pdf_link.split('/')[-1]
        if file_name[-3:] != 'pdf':
            file_name += '.pdf'
        file_names.append(file_name)
        pdf = requests.get(pdf_link).content
        with open(file_name, 'wb') as f:
            f.write(pdf)
        sleep(3)

    return file_names
