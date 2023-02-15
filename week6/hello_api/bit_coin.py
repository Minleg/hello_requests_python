import requests
from pprint import pprint

try:
    response = requests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()
    
    data = response.json()
    # pprint(data)
    
    rate = data['bpi']['USD']['rate_float']
    print(f'Current rate of 1 bitcoin to USD is {rate}')
    
    bitcoin = float(input('Enter the numbe rof bitcoin: '))
    bitcoin_value_in_dollars = bitcoin * rate
    
    print(f'{bitcoin} Bitcoin is equivallent to ${bitcoin_value_in_dollars}')
    
except Exception as e:
    print(e)
