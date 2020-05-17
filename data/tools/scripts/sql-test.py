# -- coding: utf-8 --
from bs4 import BeautifulSoup
import requests
import re

errors = [
    '"=""'
]

def get(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    for form in soup.select('form'):

        print(str(form['id']))
        print(str(form['method']))
        print(str(form['action']))

        for inputs in soup.select('input'):
            print(str(inputs['name']))
        

get("127.0.0.1:8080")