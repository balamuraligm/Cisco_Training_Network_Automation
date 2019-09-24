#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import paramiko, time, sys

client = paramiko.SSHClient()

Addr = sys.argv[1]
usern = sys.argv[2]
passw = sys.argv[3]


