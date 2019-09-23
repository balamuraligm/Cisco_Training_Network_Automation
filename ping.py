#!/usr/bin/python3

from subprocess import getoutput
import sys
from time import sleep
data =sys.argv[1:]

for i in data:
    print ("Ping Request for ",i)
    print (getoutput("ping -c 3 "+i))
    print ('======================')
    print ('======================')

