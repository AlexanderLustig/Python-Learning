import json
import requests

query = input("Please enter your IP address: ")
r = requests.get(f'http://ip-api.com/json/{query}')

with open("IP_JSON_PROJECT.json", "w") as f:
    json.dump(r.json(), f, indent=4)