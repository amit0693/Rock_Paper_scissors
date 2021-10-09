import random
from RPS_ASCII import rock
from RPS_ASCII import paper
from RPS_ASCII import scissors
player1=int(input("What you choose?type 0 for Rock, 1 for Paper or 2 for Scissors:"))
computer= int(random.randint(0,2))
if player1==computer:
    print("Its Draw")
elif player1==0 and computer==1:
    print("You choose rock" +rock +"\nI Choose paper" +paper +" You Lose")
elif player1==0 and computer==2:
    print("You choose rock" +rock +"\nI Choose scissors" +scissors +"You Win")
elif player1==1 and computer==0:
    print("You choose paper"+paper +"\nI Choose rock" +rock +"You Win")
elif player1==1 and computer==2:
    print("You choose paper"+paper +"\nI Choose scissors" +scissors +"You win")
elif player1==2 and computer==0:
    print("You choose scissors"+scissors +"\nI Choose rock"+rock +"You Lose")
elif player1==2 and computer==1:
    print("You choose scissors"+scissors +"\nI Choose paper"+paper +"You Win")
else:
    print("You choosed wrong number")

    
    
