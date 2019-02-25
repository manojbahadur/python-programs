#dictionary
d={"manoj":1234566,"a":"09876","b":35451,"c":82582,"d":43676,"e":47254}
for i in d:
	print(d[i])
for i in d:
	print(i)
print("manoj")
n=input("Enter a name:")
if n in d:
	print("Name:",n,"Num:",d[n])