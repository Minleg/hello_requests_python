import requests
from pprint import pprint

url = 'http://api.worldbank.org/v2/country/in?format=json'

data = requests.get(url).json()

capital_city = data[1][0]['capitalCity']

print(capital_city)
# pprint(data)