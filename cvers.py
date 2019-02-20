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
	while True:
		line = tn.read_until("\n")
		if "fc1" in line:
			print line
			break
	tn.write("exit\n")
	tn.close()
