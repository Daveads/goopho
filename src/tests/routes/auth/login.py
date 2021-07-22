import requests

from requests.auth import HTTPBasicAuth

response = requests.post('http://127.0.0.1:5000/login' , auth = HTTPBasicAuth('goopho', '123456'))

print(response.json())
