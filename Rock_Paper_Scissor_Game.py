import random
import sys
from enum import Enum
 
class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSOR=3

print("")
your_choice=input("Enter Choice.......\n1 for Rock\n2 for Paper or\n3 for Scissor\n")
your=int(your_choice)
if your<1 or your>3:
    sys.exit("Enter 1,2 or 3")

computer_choice=random.choice("123")
computer=int(computer_choice)

print("You Chose: "+str(RPS(your)).replace("RPS.",""))
print("Python Chose: "+str(RPS(computer)).replace("RPS.",""))


if your==1 and computer==3:
    print("🏆You Win!!!")
elif your==2 and computer==1:
    print("🏆You win!!!")
elif your==3 and computer==2:
    print("🏆You Win!!!")
elif your==computer:
    print("📍😯Tie!!!")
else:
    print("🐍Python Wins!!!")