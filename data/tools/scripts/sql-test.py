# -- coding: utf-8 --
from bs4 import BeautifulSoup
import requests
import re

def get(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    for item in soup.select('input'):

        print(str(item['name']))
        
get("http://0.0")