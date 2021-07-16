# import requests module
import requests
from requests.auth import HTTPBasicAuth
  
# Making a get request
response = requests.get('http://127.0.0.1:5000/login / user, ',
            auth = HTTPBasicAuth('osamede', '12345'))
  
# print request object
print(response)
