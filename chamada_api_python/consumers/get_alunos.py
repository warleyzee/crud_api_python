import requests
from requests import status_codes
from pprint import pprint
from get_token import token

_print = print
pprint = print

url = "http://127.0.0.1:3001/alunos"

headers = {
    "Authorization": token
}

response = requests.get(url=url, headers=headers)



if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)

    response_data = response.json()

    for alunos in response_data:
        print(alunos['id'], alunos['nome'])
else:
    print("ERROR!!!")
    print(response.status_code)
    print(response.reason)
    print(response.json())