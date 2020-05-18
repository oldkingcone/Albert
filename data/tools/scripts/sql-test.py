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

session = HTMLSession()

def get(url):
    # GET request
    res = session.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.find_all("form")

def prepare(form, inject):

    payload = {}

    inputs = []

    action = form.attrs.get("action")
    method = form.attrs.get("method")

    for input_tag in form.select("input"):

        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = inject # Value
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    payload["action"] = action
    payload["method"] = method
    payload["inputs"] = inputs

    return payload


for error in errors:

    forms = get("http://localhost:8080/sql.php")

    for i, form in enumerate(forms, start=1):
        form_details = prepare(form, error)
        print(form_details)