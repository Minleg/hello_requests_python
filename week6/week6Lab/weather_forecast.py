import requests
import os
from pprint import pprint
from datetime import datetime

key = os.environ.get('WEATHER_KEY')

url = 'https://api.openweathermap.org/data/2.5/forecast'

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('Sorry, could not get weather') # may be the city doesn't exist in the country
    else:
        list_of_forecast = weather_data['list'] # gets list of the weather information every three hours of the next five days 
        print('Date         Time        Temperature     Wind Speed      Weather Description')
        for forecast in list_of_forecast:
            temp = forecast['main']['temp']
            timestamp = forecast['dt']
            forecast_date = datetime.fromtimestamp(timestamp)
            date_adjusted =  forecast_date.strftime('%m/%d/%Y %H:%M') # adjusted date and time format
            am_or_pm = get_am_or_pm(date_adjusted)
            weather_description = forecast['weather'][0]['description']
            wind_speed = forecast['wind']['speed']
            print(f'{date_adjusted}{am_or_pm} {temp:>13}F{wind_speed:>15}         {weather_description}')

def get_location():
    """ This method gets the city and the two alphabet code of the country it resides in and returns the location"""
    city, country = '', ''
    while len(city) == 0 or not city.isalpha():
        city = input('Enter the name of the city: ').strip()
    
    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()
        
    location = f'{city},{country}'
    return location

def get_current_weather(location, key):
    """ this method connects to the api to get weather forecast data, it returns a tuple of the response data and the exception if any """
    try:
        query = {'q': location, 'units': 'metric', 'appid':key}
        response = requests.get(url, params=query)
        response.raise_for_status() # Raise exception for 400 or 500 errors
        data = response.json() # this may error too, if response is not JSON
        return data, None
    except Exception as ex:
        return None, ex

def get_am_or_pm(date_adjusted):
    """ This method returns string 'AM' or 'PM' depending on what the local time is: """
    am_or_pm = 'AM' # initialiazation
    date_time_list = date_adjusted.split(' ') # date and time as seperate element as list
    hour = date_time_list[1] # gets time in format %H:%M
    hour_list = hour.split(':') 
    hour = hour_list[0] # gets the hour value
    
    if int(hour) >= 12:
        am_or_pm = 'PM'
    return am_or_pm

if __name__ == '__main__':
    main()
