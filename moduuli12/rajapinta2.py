import json

import requests

jes = input("Anna paikkakunnan nimi: ")

pyynto = f"http://api.openweathermap.org/geo/1.0/direct?q={jes}&limit=5&appid=27a2748c736d3d6d5f5126a2b72d2e02"


vastaus = requests.get(pyynto).json()

print(json.dumps(vastaus, indent=4))

for a in vastaus:
    latitude = a["lat"]
    longtitude = a["lon"]

pyynto = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longtitude}&exclude=minutely,hourly&appid=27a2748c736d3d6d5f5126a2b72d2e02"

vastaus = requests.get(pyynto).json()

print(json.dumps(vastaus, indent=4))

print(vastaus["daily"][0]["temp"]["day"])
print(vastaus["daily"][0]["weather"][0]["description"])