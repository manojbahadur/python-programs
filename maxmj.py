def max(a,b,c):
	if a>b and b>c:
		l=a
	elif b>a and a>c:
		l=b
	else:
		l=c
	return l
 
print("Enter three values")
a=input()
b=input()
c=input()
l=max(a,b,c)
print("largest is",l)
