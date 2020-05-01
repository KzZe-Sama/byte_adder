import functions2
import functions3
# Function that asks input from user of a number 
# Type casting the inputed value and checking if the value is less than 0 or greater than 255
# the fucntion is return type
addValue=[0,0,0,0,0,0,0,0]
def StepTwoFunction(userInputNumber):
	while(userInputNumber<0 or userInputNumber>255):
		userInputNumber=int(input("Error![The Inputed Number Exceeds Range]\nEnter a number within range\n"))
	return userInputNumber
# This function pulls remainder of the inputed number and stores the value starting from last index of our list
def RevDecimalToBinary(num):
	bit=[0,0,0,0,0,0,0,0]
	counter=0
	while counter!=8:
		remainder=num%2
		bit[7-counter]=remainder
		num=num//2
		counter+=1
	return bit
# adding the two inputed values through base 2 
def checkTotal(a,b):
	if(a+b<255):
		# Storing the values into arrayList of 8 bit
		storeForFirst=RevDecimalToBinary(a)
		storeForSecond=RevDecimalToBinary(b)
		# # Calling main function with the algorithm of logic gates
		functions3.addThem(storeForFirst,storeForSecond,addValue)
		# # calling display function
		functions2.display(a,b,storeForFirst,storeForSecond,addValue)
	else:
		print("Their Sum Exceeds More than 8 Bit")

