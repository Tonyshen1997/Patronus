import requests
import json
import base64

url = 'http://127.0.0.1:5000/'
files = {'image': open('1.jpg', 'rb')}
r = requests.post(url, files=files)
print(r.json())
