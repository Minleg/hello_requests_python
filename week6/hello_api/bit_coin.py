import requests

# try:
#     response = requests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
#     response.raise_for_status()
    
#     data = response.json()
#     # pprint(data)
    
#     rate = data['bpi']['USD']['rate_float']
#     print(f'Current rate of 1 bitcoin to USD is {rate}')
    
#     bitcoin = float(input('Enter the number of bitcoin: '))
#     bitcoin_value_in_dollars = bitcoin * rate
    
#     print(f'{bitcoin} Bitcoin is equivallent to ${bitcoin_value_in_dollars}')
    
# except Exception as e:
#     print(e)

def main():
    bitcoin_amount = get_bitcoin_amount()
    bitcoin_value_in_dollars = convert(bitcoin_amount)
    output(bitcoin_amount, bitcoin_value_in_dollars)
    
    

def get_bitcoin_amount():
    bitcoin = float(input('Enter the number of bitcoin: '))
    return bitcoin

def request_bitcoin_rate():
    try:
        response = requests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        return data  
    except Exception as e:
        return None

def extract_rate(data):
    rate = data['bpi']['USD']['rate_float']
    return rate

def convert(amount):
    response = request_bitcoin_rate()
    exchange_rate = extract_rate(response)
    return amount * exchange_rate

def output(bitcoin, bitcoin_value_in_dollars):
    print(f'{bitcoin} Bitcoin is equivallent to ${bitcoin_value_in_dollars}')
    
if __name__ == '__main__':
    main()


    

    
    