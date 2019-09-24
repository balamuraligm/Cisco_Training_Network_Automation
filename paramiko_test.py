#!/usr/local/bin/python3

import paramiko,time

# Using as SSH client
client = paramiko.SSHClient()

#Auto Adjust host key verification with Yes or No.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connecting to Cisco IOS remotely.

Addr = input("Enter the router IP address ")
usern = 'root'
passw = 'cisco123'

# Initiated an SSH Connetion. If there is no error message, it is working fine.
client.connect(Addr, username = usern, password=passw, allow_agent = False, look_for_keys=False)


#Below is to invoke the shell
device_access = client.invoke_shell()

#sendin the commands
device_access.send("conf t \n")
time.sleep(1)
device_access.send("interface loop 0 \n")
time.sleep(.5)
device_access.send("ip address 10.10.10.10 255.255.255.255\n")

device_access.send("no shut \n")


time.sleep(1)
device_access.send("do show ip interface brief \n")
time.sleep(1)

#receiving the output
output = device_access.recv(60000)
# there is no limit on amount of data that we can receive. Max limit is bandwidth.
print(type(output))


#decoding byte like string into normal string
print(output.decode('ascii'))
print(type(output.decode('ascii')))



