"""
Query params : sunt niste parametrii pe care ii putem trimite prin URL, dupa ultimul / (dupa semnul intrebarii)

"""
import requests
from pprint import pprint

query_params = {
    'q': 'phone',
    'select': 'title,price,description'
}

url = 'https://dummyjson.com/products/search'
response = requests.get(url, params=query_params)
print(response.status_code)
pprint(response.json())