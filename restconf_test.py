#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3


import requests

from requests.auth import HTTPBasicAuth

cred = HTTPBasicAuth("root", "cisco123")


headers = {'Accept': 'application/json'}

url = 'http://192.168.2.131/level/15/exec/-/show/ip/inter/brief/CR'


output = requests.get(url,headers=headers,auth=cred)

print(output)
print("--------------------------------")

print(output.text)
