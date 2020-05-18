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
    soup = BeautifulSoup(res.text, "html.parser")
    prepare(soup.find("form"))

def prepare(form):

    print(form)

    payload = {}

    action = form.attrs.get("action")
    method = form.attrs.get("method")

    inputs = []
    # For each error based SQL input
    for error in errors:
        for input_tag in form.select("input"):

            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value = error
            inputs.append({"type": input_type, "name": input_name, "value": input_value})

            payload["action"] = action
            payload["method"] = method
            payload["inputs"] = inputs

            print(payload)

            return payload

        else:
            print("[SQL] >> No error based input defined?")

get("http://0.0.0.0:6779")