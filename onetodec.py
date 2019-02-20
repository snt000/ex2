#!/usr/bin/python3
mask = input ("Enter CIDR mask: ")
cidr = mask.replace("/", "")
netmask = '.'.join([str((0xffffffff << (32 - int(cidr)) >> i) & 0xff)
			 for i in [24, 16, 8, 0]])
print (netmask)
