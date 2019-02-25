import random
min = 1
max = 6

r="yes"

while r=="yes" or r=="y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))

    r=input("Roll the dices again?")