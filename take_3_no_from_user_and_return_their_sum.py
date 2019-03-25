#take 3 no from user and return their sum, return 0 if any two nos are same
def funno(n1,n2,n3):
	if n1==n2 or n2==n3 or n1==n3:
		return 0
	else:
		return n1,n2,n3
n1 = int(input("Enter 1st no: "))
n2 = int(input("Enter 2nd no: "))
n3 = int(input("Enter 3rd no: "))
s = n1+n2+n3
print("Sum=",s)	
funno(n1,n2,n3)