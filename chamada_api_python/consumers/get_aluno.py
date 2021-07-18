import requests
from requests import status_codes
from pprint import pprint
from get_token import token

_print = print
pprint = print

url = "http://127.0.0.1:3001/alunos/1"

headers = {
    "Authorization": token
}

response = requests.get(url=url, headers=headers)



if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)

    response_data = response.json()
    print(response_data['nome'], response_data['sobrenome'], response_data['email'], response_data['idade'], response_data['peso'], response_data['altura'])
else:
    print("ERROR!!!")
    print(response.status_code)
    print(response.reason)
    print(response.json())