# -- coding: utf-8 --
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import re

errors = [
    "SELECT @@version",
    "query",
    "admin",
    "1234",
    "test"
]

session = HTMLSession()

def get(url):
    # GET request
    res = session.get(url)
    res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def prepare(form):

    payload = {}

    inputs = []

    action = form.attrs.get("action")
    method = form.attrs.get("method")

    for input_tag in form.select("input"):

        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "") # Value
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    payload["action"] = action
    payload["method"] = method
    payload["inputs"] = inputs

    return payload

url = "http://localhost:8080/sql.php"

forms = get(url)

for form in forms:

    form_details = prepare(form)

    data = {}

    for error in errors:

        for input_tag in form_details["inputs"]:

            if input_tag["type"] == "hidden":
                data[input_tag["name"]] = input_tag["value"]
            elif input_tag["type"] != "submit":
                value = error
                data[input_tag["name"]] = value

            if form_details["method"] == "post":
                res = session.post(url, data=data)
                print(res.text)
            elif form_details["method"] == "get":
                res = session.get(url, params=data)
                print(res.text)
