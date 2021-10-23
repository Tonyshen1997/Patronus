import requests


url = 'http://127.0.0.1:5000/'
my_img = {'image': open('1.jpg', 'rb')}
r = requests.post(url, files=my_img)

print(r.json())
