# Display function to display the final value of the Binary addtion that we have done
def display(a,b,x,y,z):
	bin1=""
	bin2=""
	for value in x:
		bin1=bin1+str(value)
	for value in y:
		bin2=bin2+str(value)
	print(f"The Binary Value of {a} is ",bin1)
	print(f"The Binary Value of {b} is ",bin2)
	print(f"So, The Binary Addition of {bin1} and {bin2} is:",end="")
	for value in z:
		print(value,end="")
	print("\n")