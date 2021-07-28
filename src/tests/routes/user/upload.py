import requests

test_url = "http://127.0.0.1:5000/upload"

#token = "dc166ec2-9429-43dd-922c-1c5ce524a172"

headers = {
    'authorization': "gop-tok eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNzQzMjMwOCwianRpIjoiZjExMTQ1MzgtMDEzMi00NjRhLThjZTgtZjIyNWUzNmE2YWIwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEzNjhkNWM5LTg2ODEtNDgxNS05YzgxLTNjZTdlMDFmNjZlZCIsIm5iZiI6MTYyNzQzMjMwOCwiZXhwIjoxNjI4NjQxOTA4fQ.zOX2b-4bXfsGdZaPDdfUHzCi7OSfF1BSUWdsM-Wvw2I"}


#headers={'X-CSRF-TOKEN' :  'dc166ec2-9429-43dd-922c-1c5ce524a172'}


multiple_files = [('file', (open('1.jpeg', 'rb'))),

                      ('file', (open('0.jpg', 'rb')))]


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
