#!/usr/bin/python3

import requests

api_key = "dc191273c64946b8a070075a2261c3fb415064e9"

try:
    data = requests.get("https://api.github.com/notifications", headers={"Authorization": "token " + api_key}).json()
    print(len(data))
except:
    print("Error")
