mask = raw_input ("Enter mask: ")
mysum = 0
for x in mask.split("."):
	mysum = mysum + bin(int(x)).count("1")
print mysum
	
