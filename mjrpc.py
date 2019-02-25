import random
l=("p","r","s")
while True:
	u=input("Choose rock, paper or scissors:     " )
	c=random.choice(l)
	print("you choose: ",u,"and computer choose: ",c)
	if u=="e":
		print("Bye!..... GAME OVER.......")
		exit()
	elif c==u:
		print("Its a tie!...")
	elif c=="s" and u=="r":
		print("You won!!...")
	elif c=="p" and u=="s":
		print("You won!...")
	elif c=="r" and u=="p":
		print("You won!....")
	elif c=="s" and u=="p":
		print("You lost!..")
	elif c=="p" and u=="r":
		print("You lost!...")
	elif c=="r" and u=="s":
		print("You lost!...")

		
			

