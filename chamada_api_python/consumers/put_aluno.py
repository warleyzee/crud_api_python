import requests
from requests import status_codes
from get_token import token
from pprint import pprint
_print = print
pprint = print

url = 'http://127.0.0.1:3001/alunos/3'

atualiza_data = {
    "nome" : "rodrigo",
    "sobrenome" : "Villa",
    "email" : "rodrigo@hotmail.com",
    "idade" : 40,
    "peso" : "80.5",
    "altura" : "1.77"
}

headers = {

    "Authorization" : token
}

response = requests.put(url=url, json=atualiza_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.json())