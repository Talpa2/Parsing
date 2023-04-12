import requests
from bs4 import BeautifulSoup

res = requests.get('https://gordonua.com/rus/')
soup = BeautifulSoup(res.text, 'html.parser')

def create(soup):
    list_create = []
    for idx, item in enumerate(soup):
        title = soup[idx].getText()
        href = soup[idx].get('href', None)
        list_create.append({'title': title, 'link': href})
    return list_create

print(create(soup))
