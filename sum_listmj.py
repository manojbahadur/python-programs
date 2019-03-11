# sum of numbers of list
def sum_list(a):
	i = 0
	for e in a:
		i = i+e
	return i

a = []
n= int(input("Number of element in list"))

print("Enter the elements:")
for k in range(n):
	el = int(input())
	a.append(el)

i = sum_list(a)

print(i, "is the sum of list")
