#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import time
from ncclient import manager

device = manager.connect(host = '192.168.2.131',username = 'root', password='cisco123',port=22, allow_agent=False, look_for_keys = False, hostkey_verify=False)
print(device)

print("----------------------")
print("----------------------")

print (dir(device))
print ("---------------------")
time.sleep(1)
print(device.get_config("running"))



