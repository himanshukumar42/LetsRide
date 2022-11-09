import requests

ENDPOINT = 'http://127.0.0.1:8000/rider/2'


response = requests.get(ENDPOINT).json()
print(response['date_time'])
print(type(response['date_time']))


