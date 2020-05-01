import functions
# Creating List(Arrays) to store the Values Later
# Defining the size of the final Value list to 8 
storeForFirst=[]
storeForSecond=[]
firstNumVar=0
secondNumVar=0
flag=False
# while loop for continuity until user wants to exit
print("__________________________")
print("Welcome to Byte Adder")
print("Version:1")
print("\n")
while(flag==False):
	#Exception Handling
	try:
		#asking input user two values a and b and passing the value to the function
			print("--------Input two Decimal Values--------")
			print("Note: You can ony enter numbers starting from 0 to 255")
			firstNumVar=int(input("Please Enter the First Number\n"))
			firstNumVar=functions.StepTwoFunction(firstNumVar)
			secondNumVar=int(input("Please Enter the Second Number\n"))
			secondNumVar=functions.StepTwoFunction(secondNumVar)
			functions.checkTotal(firstNumVar,secondNumVar)
			# # Asking if user wants to continue or not
			ask=input("Do You want to Run the Program Again? (Y/N)\n")
			ask=ask.upper()
			if(ask=="Y"):
				flag=False
			else:
				print("Thank you for using this Python Program, Have a nice day!")
				print("\n")
				break
	except:
		print("Data Type ERROR!\nThe Program is meant to accept integer values only")
		print("\n")
