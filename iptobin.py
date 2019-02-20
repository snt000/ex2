"""
Takes and prints an IP address in binary
"""
ip = raw_input("Enter IP address: ")
parts = ip.split (".")
for s in parts:
	i = int(s)
	print bin(i)
	#print hex(i)
