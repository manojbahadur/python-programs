import random
l=("paper","rock","scissors")
us=0
cs=0
while True:
		u=input("Choose rock, paper or scissors:    \n " )
		c=random.choice(l)
		print("Your choice: \n",u,"\nComputer choose: \n",c)
		if us==5 or cs==5:
			print("User Score=",us)
			print("Computer score=",cs)
			if(us>cs):
				print("You won!...")
			else:
				print("computer won!..")
			exit()
		elif c=="scissors" and u=="rock":
			us=us+1
		elif c=="paper" and u=="scissors":
			us=us+1
		elif c=="rock" and u=="paper":
			us=us+1
		elif c=="scissors" and u=="paper":
			cs=cs+1
		elif c=="paper" and u=="rock":
			cs=cs+1
		elif c=="rock" and u=="scissors":
			cs=cs+1



		
			

