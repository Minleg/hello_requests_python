import requests

try:
    response = requests.get('https://catfact.ninja/fact') # requests.get() returns text, so its is converted to json with json()
    print(response.status_code)

    response.raise_for_status() # raise an exception for 400 or 500 status code
    print(response.text)
    print(response.json())

    data = response.json()

    fact = data['fact'] # fact is a key in the JSON response 
    print(f'A random cat fact is {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request.')