import random
l={"p":"paper","r":"rock","s":"scissors"}
s=("p","r","s")
us=0
cs=0
while True:
		u=input("Choose rock, paper or scissors:    \n " )
		c=random.choice(s)
		print("Your choice: \n",l[u],"\nComputer choose: \n",l[c])
		if us==5 or cs==5:
			print("User Score=",us)
			print("Computer score=",cs)
			if(us>cs):
				print("You won!...")
			else:
				print("computer won!..")
			exit()
		elif c=="s" and u=="r":
			us=us+1
		elif c=="p" and u=="s":
			us=us+1
		elif c=="r" and u=="p":
			us=us+1
		elif c=="s" and u=="p":
			cs=cs+1
		elif c=="p" and u=="r":
			cs=cs+1
		elif c=="r" and u=="s":
			cs=cs+1



		
			

