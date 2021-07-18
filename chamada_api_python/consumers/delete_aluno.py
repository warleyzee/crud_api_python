import requests
from requests import status_codes
from get_token import token
from pprint import pprint
_print = print
pprint = print

url = 'http://127.0.0.1:3001/alunos/1'

headers = {
    "Authorization": token
}

response = requests.delete(url=url, headers=headers)

if response.status_code >= 200  and response.status_code<= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.json())