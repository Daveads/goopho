import requests

test_url = "http://127.0.0.1:5000/upload"

#token = "dc166ec2-9429-43dd-922c-1c5ce524a172"

#headers = {'X-CSRF-TOKEN': token }

#headers={'X-CSRF-TOKEN' :  'dc166ec2-9429-43dd-922c-1c5ce524a172'}


test_files = {

    "file" : (open("0.jpg", "rb"),

              open("1.jpeg", "rb"),

              open("2.jpeg", "rb"),

              open("3.jpg", "rb")),

    "title" : "this is a title",

    "description" : "just testing stuffs"
}




test_response = requests.post("http://127.0.0.1:5000/upload", files=test_files)


"""
if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")
"""
