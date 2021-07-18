from os import write
import requests
from requests import status_codes
from pprint import pprint

from requests.models import Response
_print = print
print = pprint

url = 'http://127.0.0.1:3001/tokens'

data_token = {
    "email": "warleyzee@hotmail.com",
    "password": "senha_Valida"
}

response = requests.post(url= url, json= data_token)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())

    response_data = response.json()
    token = response_data['token']
    with open ('token.txt', 'w') as file:
        file.write(token)
else:
    print("ERRO!!!")
    print(response.status_code)
    print(response.reason)
    print(response.json())