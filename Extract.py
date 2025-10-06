import requests
import os
import json

def extract(city_name):
    raw_req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv('API_KEY')}&units=metric")
    json_req = json.dumps(raw_req.json(), indent=3)

    # NOTES
    # weather.main, weather.description, 
    # main.temp, main.feels_like, main.pressure,
    # wind.speed, wind.deg (Calculate in which direcion by myself), 
    # clouds.all, clouds.name

    # print(req)
    # print(json.dumps(req.json(), indent=3))
    # print(type(req.json()))