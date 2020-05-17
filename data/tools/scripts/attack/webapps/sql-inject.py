# -- coding: utf-8 --
from bs4 import BeautifulSoup
import requests

def get(url): 
    page = requests.get(url)
    contents = page.text()
    print([(element['name'], element['value']) for element in contents.find_all('input')])

get("https://www.torrentmac.net/")