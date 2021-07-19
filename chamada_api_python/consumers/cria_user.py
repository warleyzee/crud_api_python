import requests
from requests import status_codes
from pprint import pprint
_print = print
print = pprint

from requests import status_codes

url = 'http://127.0.0.1:3001/users'

user_data = {
    "nome":"Vila",
    "password": "123456",
    "email": "rodrigo@hotmail.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print(response.json())
else:
    print("ERROR!!!!")
    print(response.status_code)
    print(response.reason)
    print(response.json())