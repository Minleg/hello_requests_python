# Example URL
# https://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&appid=2dadae09d640439cd2837e7d024ee036
import os
import requests
from datetime import datetime
from pprint import pprint

key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units' : 'imperial', 'appid':key}

url = 'https://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
# pprint(data)

list_of_forecast = data['list']

for forecast in list_of_forecast:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f'At {forecast_date} the temperature will be {temp}F')