#!/usr/bin/env python

import requests

test_url = "http://127.0.0.1:5000/upload"

#token = "dc166ec2-9429-43dd-922c-1c5ce524a172"

headers = {
    'authorization': "gop-tok  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNzk2ODkxNCwianRpIjoiNGUyNGQ3ZWMtMzA2NC00MTQ4LWE2MzAtNWY1OGQ5MmQ2MGE4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImYwZDVlYjQ4LWFhZDUtNDY2NC1hMmYxLTNmYzM1Mzk2ZDZjZCIsIm5iZiI6MTYyNzk2ODkxNCwiZXhwIjoxNjI5MTc4NTE0fQ.A8xDVV9fJ3yd5zDEnc3lJaQOyUqaUPa1Yuayq-lYFLM"}      
    
#headers={'X-CSRF-TOKEN' :  'dc166ec2-9429-43dd-922c-1c5ce524a172'}


multiple_files = [('file', (open('dave.jpeg', 'rb'))),

                      ('file', (open('dd.jpg', 'rb')))]


#files = {'file': open('0.jpg', 'rb')}
#"http://127.0.0.1:5000/upload", headers=headers


myobj = {'title': 'testing',
        'description' : "just testing"
}


test_response = requests.post(url=test_url, headers=headers, files=multiple_files, data=myobj)



if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
    
    
else:
    print("Something went wrong!")
    print(test_response.json())
