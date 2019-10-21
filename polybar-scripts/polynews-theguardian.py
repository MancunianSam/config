#!/usr/bin/python3

import requests
import random

api_key = "845ce90d-7f1d-4916-b262-7bedddf05f51"

try:
    data = requests.get("https://content.guardianapis.com/search?api-key="+api_key).json()
    index = random.randint(0,9)	
    sectionName = data['response']['results'][index]["sectionName"]
    if sectionName != "Sport" and sectionName != "Football" and sectionName != "Life and style":
        webTitle = data['response']['results'][index]["webTitle"]
        f = open("/home/sam/.config/polybar-scripts/current-url", "w")
        f.write(data['response']['results'][index]["webUrl"])
        f.close()

        print(sectionName+': '+webTitle)
	
except requests.exceptions.RequestException as e:
    print ('Something went wrong!')
