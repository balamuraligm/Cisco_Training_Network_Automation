#!/usr/bin/python3


import sys
from time import sleep
data =sys.argv[1:]
sum = 0
for i in data:
    sum = sum +int(i)

print (" The sum of the numbers is ",sum)

