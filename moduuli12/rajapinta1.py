import json

import requests


pyynto = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyynto).json()

print(json.dumps(vastaus, indent=2))

print(vastaus["value"])