import requests
import json
import base64

url = 'http://34.145.220.144'
files = {'image': open('1.jpg', 'rb')}
r = requests.post(url, files=files)
print(r.json())
