import requests
import json
import os

BASE_URL = "https://api.pipefy.com/graphql"
TOKEN = os.environ['TOKEN_STRING']

payload = {
    "query": 
        "{ table_records(table_id: 303034125){ edges { node { title record_fields{ name value } } } } }"
}

headers = {
    "accept": "application/json",
    "Authorization":f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(BASE_URL, json=payload, headers=headers)

dict_response = json.loads(response.text)['data']['table_records']['edges']

print(dict_response)
