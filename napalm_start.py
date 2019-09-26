#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from napalm import get_network_driver

#Getting the driver
driver = get_network_driver('ios')

#Connecting to the device
device =driver("192.168.2.131", "root", "cisco123")

print([i for i in dir(device) if 'load' in i])

# opening the session with the device.
device.open()
'''
device.load_merge_candidate(filename='/Users/mnagaboi/Documents/Udemy/Cisco_Training_Network_Automation/CSR_con.txt')

# To compare the ouputs before merging and after merging
print (device.compare_config())

c = input('Confirm the configuration changes with Y | N  ')

if(c=='Y' or c=='y'):
	#Committing the configuration
	print("Committing the configuration")
	device.commit_config()
elif(c=='N' or c=='n'):
	print("Dicarding the configuration")
	device.discard_config()
else:
	print("Choose a valid choice")
'''

# To rollback the recent commit.
device.rollback()

#closing the connection
device.close()

