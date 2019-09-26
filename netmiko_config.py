#!/usr/local/bin/python3

#from netmiko import ConnectHandler
import netmiko

Device1 = {
	'username': 'root',
	'password': 'cisco123',
	'device_type': 'cisco_ios',
	'host': '192.168.2.132'
}

device_connect = netmiko.ConnectHandler(**Device1)
print(device_connect)

#print([i for i in dir(device_connect) if 'send' in i])
'''
config = ["hostname CSR1000v-2", "username hello privi 10 password cisco", "inter loop 0", "ip address 20.20.20.20 255.255.255.255" , "no shut"]
output = device_connect.send_config_set(config)
print(output)'''
output = device_connect.send_config_from_file('CSR_con.txt')
print(output)

command = ["show ip interface brief"]
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

