import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def extract():
    city_name = ""
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv('API_KEY')}")
