import requests

ENDPOINT = 'http://127.0.0.1:8000/'


response = requests.get(ENDPOINT, params={"param1": "nothing"}, json={"name": "himanshu"})
print(response.text)

