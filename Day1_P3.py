#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from os import mkdir
from os import rmdir
from time import ctime, sleep
# only importing desired functions.
from subprocess import getstatusoutput, getoutput

option = '''
press 1 to check date and time
press 2 to run any command in your system
press 3 to ceate a directory
press 4 to start train
press 5 to ping any website
press 6 to remove the directory
'''
print (option)

choice = int(input("Give the input"))

print("You have chosen ",choice, type(choice))

if choice == 1:
    print (ctime())

elif choice == 2:
    CLI_to_run = input("Specify the command that we need to run")
    print (getoutput(CLI_to_run))

elif choice == 3:
    Directory_name = input ("Specify the directory name")
    mkdir(Directory_name)
    print (Directory_name, " got created")

elif choice == 6:
    Directory_name = input ("Specify the directory name")
    rmdir(Directory_name)
    print (Directory_name, "got deleted")

elif choice == 4:
    print (getoutput('sl'))

elif choice == 5:
    website = input("Enter the website name to ping")
    print (getoutput("ping -c 5 "+website))

else:
    print( "Invalid Choice")


