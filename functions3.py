def addThem(x,y,z):
	carryIn=0
	for i in range(7,-1,-1):
		# the following algorithm is based on the logic gate prescribed as by the Coursework
		a=x[i]
		b=y[i]
		and_1=a&b
		xor_1=a^b
		Sum=xor_1^carryIn
		and_2=xor_1&carryIn
		carryOut=and_1|and_2 
		carryIn=carryOut
		z[i]=Sum
		