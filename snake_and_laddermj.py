#snake and ladder 
import random
p=0
d=0
#dictionary
snl={8:37,13:34,40:68,52:81,76:97,11:2,25:4,38:9,65:46,89:70,93:64}
#function to roll dice
def rolldice():
	return random.randint(1,6)
#get 1 or 6 on the dice to enter game
while True:
	r=input("press r to roll, q to quit:")
	if r=="r":
		d=rolldice()
	if d==6 or d==1:
		p=d
		print("you are in the game ,at:",p)
		break
while True:
	r=input("press r to roll,q to quit:")
	if r=="r":
#knowing the position
		d=rolldice()
		p=p+d
		print("you are at:",p)
	if p==100:
		print("you won:")
		exit()
#for winning num
	if p>100:
		p=p-d
		print("you need to get",100-p,"to reach home:")

	if p in snl:
		if p<snl[p]:
			print("lucky!climed a ladder:",p)
		else:
			print("eaten by a snake:")
		p=snl[p]
		print("you are at:",p)
	elif r=="q":
exit()