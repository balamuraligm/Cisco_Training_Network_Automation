#!/usr/local/bin/python3

import paramiko,time,sys

# Using as SSH client
client = paramiko.SSHClient()

#Auto Adjust host key verification with Yes or No.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connecting to Cisco IOS remotely.
device_ip = ['192.168.2.131', '192.168.2.131', '192.168.2.131']

usern = 'root'
passw = 'cisco123'




# Initiated an SSH Connetion. If there is no error message, it is working fine.
for i in device_ip:
    client.connect(i, username = usern, password=passw, allow_agent = False, look_for_keys=False)
    #Below is to invoke the shell
    device_access = client.invoke_shell()

    #sendin the commands'
    device_access.send("terminal length 0 \n")
    time.sleep(1)
    device_access.send("show run \n")
    time.sleep(1)

    #receiving the output
    output = device_access.recv(60000)
    # there is no limit on amount of data that we can receive. Max limit is bandwidth.
    #print(type(output))


    #decoding byte like string into normal string
    #print(output.decode('ascii'))
    with open(i+time.ctime(), 'w') as f:
        f.write(output.decode('ascii'))
    time.sleep(1)

