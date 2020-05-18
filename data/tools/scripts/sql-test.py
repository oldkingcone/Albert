# -- coding: utf-8 --
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import re

errors = [
    "' OR ''='",
    "query",
    "admin",
    "1234",
    "test"
]

inputs = []

session = HTMLSession()

def get(url):
    # GET request
    res = session.get(url)
    soup = BeautifulSoup(res.html.html, "html.parser")
    prepare(soup.find_all("form"))

def prepare(form):

    print(form)

    payload = {}

    action = form.get("action").lower()
    method = form.get("method").lower()

    inputs = []

    for input_tag in form.find_all("input"):
        # For each error based SQL input
        for error in errors:

            print(error)
        
        else:
            print("[SQL] >> No error based input defined?")

get("http://0.0.0.0:6779")