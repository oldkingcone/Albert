# -- coding: utf-8 --
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import re

session = HTMLSession()

def get(url):
    res = session.get(url) # Pull page source.
    res.html.render() # Javascript.
    soup = BeautifulSoup(res.html.html, "html.parser") # Parse page source.
    return soup.find_all("form") # Return all elements in form.

def prepare(form):

    params = {} # Dictonary of inputs, method and action of the current form.

    inputs = [] # List of all inputs.

    # Grab form action and method.
    action = form.attrs.get("action")
    method = form.attrs.get("method")
    # Select each input in form.
    for input_tag in form.select("input"):
        # Categorize and get input value.
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "") # Value
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    # Append to dictonary.
    params["action"] = action
    params["method"] = method
    params["inputs"] = inputs

    #print(str(params["inputs"][1])) # Debugging.

    # Return dictonary of values.
    return params

# URL
url = "http://localhost:8080/sql.php"

# Pull all forms from URL.
forms = get(url)

# For each form.
for form in forms:
    # Parse information.
    form_details = prepare(form)
    # Dictonary of values.
    data = {}
    # Handle the form inputs and their values.
    for input_tag in form_details["inputs"]:
        # If input is hidden, leave value the same.
        if input_tag["type"] == "hidden":
            data[input_tag["name"]] = input_tag["value"]
        # If the input is not a submittion, assign new value.
        elif input_tag["type"] != "submit":
            value = "x"
            data[input_tag["name"]] = value

    if form_details["method"] == "post":
        # SQLMap POST command.
        print("POST")
    elif form_details["method"] == "get":
        # SQLMap GET command.
        print("GET")
