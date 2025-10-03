import requests
import os
import json

def extract(city_name):
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv('API_KEY')}")
    print(req)
    print(json.dumps(req.json(), indent=3))
    print(type(req.json()))