#!/usr/bin/python
#Telnet to a Cisco device sh run
import getpass
import sys
import telnetlib
import time

#Changed IP to a cisco device
hosts=["192.168.122.11",
	"192.168.122.11",
	"192.168.122.11"]

user = raw_input("Enter your remote account: ")
password = getpass.getpass()

for host in hosts:
	print host
	tn = telnetlib.Telnet(host)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")

	tn.write("terminal length 0\n")
	tn.write("sh version | include Version\n")
	lines = tn.read_until("fc1")
#	print lines[len(lines)-1] # This does last character not last line
	mylist = lines.split("\n")
	print mylist[len(mylist)-1]
	tn.write("exit\n")
	tn.close()
