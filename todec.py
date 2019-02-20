mask = raw_input ("Enter CIDR mask: ")
cidr = mask.replace("/", "")
if int(cidr) <= 8:
	print str((0xff << (8-int(cidr))) & 0xff) + ".0.0.0"
if int(cidr) <= 16:
	print "255." + str((0xffff << (16-int(cidr))) & 0xff) + ".0.0"
if int(cidr) <= 24:
	print "255.255." + str((0xffffff << (24-int(cidr))) & 0xff) + ".0"
if int(cidr) <= 32:
	print "255.255.255." + str((0xffffffff << (32-int(cidr))) & 0xff)
