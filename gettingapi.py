import requests
import json

response = requests.get("http://127.0.0.1:5000/")

def jprint(obj):
    #to create a python object
    data = json.dumps(obj, sort_keys= True , indent= 4)
    print(data)

jprint(response.json())