import requests
from pprint import pprint
import os
import logging

""" Configure your logger. filenmae - where to write to. otherwise logs write to the console 
level is the minimum log level that is recorded. DEBUG means log everything.
format sets the format of the string that is recorder for each log event."""
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logging.info - logging.exception - logging.error

key = os.environ.get('WEATHER_KEY') # to get the key set on your OS

# unit can be metric for celcius, if not specified kelvin, imperial is for farenheight. appid is API key
url = 'https://api.openweathermap.org/data/2.5/weather'

# pprint(data)

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('Sorry, could not get weather') # may be the city doesn't exist in the country
        logging.debug(f'location not found "{error}"')
    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature is {current_temp}C')

def get_location():
    city, country = '', ''
    while len(city) == 0 or not city.isalpha():
        city = input('Enter the name of the city: ').strip()
    
    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()
        
    location = f'{city},{country}'
    return location

def get_current_weather(location, key):
    """ this method connects to the api to get weather data, it returns a tuple of the response data and the exception if any """
    try:
        query = {'q': location, 'units': 'metric', 'appid':key}
        response = requests.get(url, params=query)
        response.raise_for_status() # Raise exception for 400 or 500 errors
        data = response.json() # this may error too, if response is not JSON
        return data, None
    except Exception as ex:
        logging.debug(f'Unable to connect to api {ex}')
        logging.debug(f'Response Text: {response.text}') # added for debugging
        return None, ex

def get_temp(weather_data):
    try:
        temp = weather_data['main']['temp']
        return temp
    except KeyError as ke:
        logging.debug(f'This data is not in the format expected: {ke}')
        return 'Unknown'

if __name__ == '__main__':
    main()

        
