#!/usr/local/bin/python3

#from netmiko import ConnectHandler
import netmiko

Device1 = {
	'username': 'root',
	'password': 'cisco123',
	'device_type': 'cisco_ios',
	'host': '192.168.2.131'
}

device_connect = netmiko.ConnectHandler(**Device1)
print(device_connect)

#print([i for i in dir(device_connect) if 'send' in i])


command = ["show ip interface brief", "show ipp"]

for i in command:
	print ("Sending command ",i)
	print ("---------------------------------")
	output = device_connect.send_command(i)
	print(output)

'''
cisco_CSR = {
    'device_type': 'cisco_ios',
    'host':   '192.168.2.131',
    'username': 'root',
    'password': 'cisco123',
    'port' : 22          # optional, defaults to 22
}
'''

