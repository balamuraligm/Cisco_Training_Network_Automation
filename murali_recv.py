#!/usr/bin/python3

import socket, time

# Checking for functions related to socket
print ([i for i in dir(socket) if 'socket' in i])

# creation of UDP socket
# IPv4 socket will be IPv4 + 2 bytes port
# IPv6 socket will be IPv6 + 2 bytes port

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#                   For IPv4       For UDP socket

s.bind(("", 8894))
# bind will accept tuple format for IP and port.

'''
This is for sender only.
Enter input message

message = input("enter the data to send")
# need to convet data into byte like string.
msg = message.encode('ascii')
s.sendto(msg,("Target IP", Port number))
s.close()
'''
while True:
    Data_received= s.recvfrom(1000) # here 1000 is the buffer size.
    print ("The data is ", Data_received[0])
    print ("The ADDRESS is ", Data_received[1])
    message = input ('Enter reply')
    new_msg = message.encode('ascii')
    s.sendto(new_msg,Data_received[1])
   

s.close() 

