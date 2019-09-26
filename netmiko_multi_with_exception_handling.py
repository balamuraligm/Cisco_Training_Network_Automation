#!/usr/local/bin/python3

#from netmiko import ConnectHandler
import netmiko
from getpass import getpass
'''sec = []
for i in [1,2]:
	sec.append(getpass("Please enter the password for device"))

print(sec)'''
sec= getpass("Please enter the password for device")
Device1 = {
	'username': 'root',
	'password': sec,
	'device_type': '1cisco_ios',
	'host': '192.168.2.131'
}
Device2 = {
        'username': 'root',
        'password': sec,
        'device_type': 'cisco_ios',
        'host': '192.168.2.132'
}

for i in [Device1, Device2]:
	try :
		print ("-----------------------------------------")
		print ("Connecting to the device of type", i['device_type'], "having IP address as", i['host'])
		print ("-----------------------------------------")
		print ("-----------------------------------------")	
		print ("-----------------------------------------")
		device_connect = netmiko.ConnectHandler(**i)
		#print(device_connect)
		#print ("Sending command ",i)
		#print ("---------------------------------")
		output = device_connect.send_command("show ip interface brief")
		print(output)
		print ("-----------------------------------------")
	except netmiko.ssh_exception.NetMikoTimeoutException :
		print("Please check the IP address or network related issues for", i['host'])

	except netmiko.ssh_exception.NetMikoAuthenticationException:
		print("Authentication failure observed for ",i['host']," Please check the username/ password credentials")
	except ValueError:
		print ("Make sure that valid device type is specified for ", i['host']) 

