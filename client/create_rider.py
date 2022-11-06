import requests
from datetime import datetime, timedelta
import json

ENDPOINT = 'http://127.0.0.1:8000/rider/'

data = {
    "name": "Sanju Gautam",
    "description": "This should not be required field",
    "from_location": "Chandigarh",
    "to_location": "Jaipur",
    "date_time": str(datetime.now() + timedelta(days=2))
}
response = requests.post(ENDPOINT, json=data)
print(response.json())
