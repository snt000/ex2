#!/usr/bin/python
#Telnet to a Cisco device sh run
import getpass
import sys
import telnetlib

#Changed IP to a cisco device
host="192.168.122.11"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

#Note change of login prompt
tn.read_until("Username: ")
tn.write(user + "\n")
if password:
	tn.read_until("Password: ")
	tn.write(password + "\n")

#sh run requires enable
tn.write("enable\n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("conf t\n")
tn.write("hostname iwozhere2\n")
tn.write("exit\n")
tn.write("exit\n")

print tn.read_all()
