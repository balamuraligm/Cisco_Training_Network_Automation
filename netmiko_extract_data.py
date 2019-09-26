


import netmiko

Device1 = {
	'username' : 'root',
	'password' : 'cisco123',
	'host' : '192.168.2.131',
	'device_type' : 'cisco_ios'
}

device_connect = netmiko.ConnectHandler(**Device1)

output1 = device_connect.send_command("show ip interface brief")
print (output1)



#output2 = device_connect.send_command("show ip interface brief",use_textfsm=True)
output3 = device_connect.send_command("show ip interface brief", use_textfsm=True)
#print(output3)
'''
for i in output3:
	print("The interface ",i['intf'], "has IP address of",i['ipaddr'], "and is in ", i['status'], "state")
'''

for i in output3:
	print (i)

