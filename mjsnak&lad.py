import random
l={8:37,11:2,13:34,28:4,38:9,40:68,65:46,52:81,89:70,93:64,76:97}
p=random.choice([2,8,11,34,38,89,93,52])
print("You got",p)
if p in d:
	if p>d[p]:
		print("Snake")
	else:
		print("Ladder")
		print("You can go to",d[p])