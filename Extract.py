import requests
import os
import json

def extract(city_name):
    raw_req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv('API_KEY')}&units=metric")
    json_req = raw_req.json()
    
    # print(json_req)
    # print(type(json_req))
    return json_req

    # print(req)
    # print(json.dumps(req.json(), indent=3))
    # print(type(req.json()))