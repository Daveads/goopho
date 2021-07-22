import requests

response = requests.post('http://127.0.0.1:5000/signup', json={"name": "Adejumo David Adewale",
                                                    "username" : "daveads",
                                                    "email" : "the.asaftest@gmail.com",
                                                    "password" : "12345"
                                                   })

print(response.json())
