import requests
from requests import status_codes
from pprint import pprint
from get_token import token
_print = print
pprint = print

url = "http://127.0.0.1:3001/alunos"

aluno_data = {
    "nome" : "Villa",
    "sobrenome" : "Nova",
    "email" : "villa@hotmail.com",
    "idade" : 29,
    "peso" : "110.05",
    "altura" : "1.81"
}

headers = {
    'Authorization' : token
}

response = requests.post(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print("ERROR!!!")
    print(response.status_code)
    print(response.reason)
    print(response.json())
