# CONDITIONALS -------------
# The if, else and elif statements are used to perform different
# actions based off of conditions
# Comparison Operators : ==, !=, >, <, >=, <=

#age = 22
#if age<16:
    #print("not eligible to drive")
#else:
    #print("eligble to drive")

import random;
player = input("Choose")
player = player.lower()
print ("You choose: "+ player);



computerInt = random.randint(0,2);
if computerInt == 0:
    Computer = "rock"
    print("Computer = choose rock")
elif computerInt == 1:
    Computer =  "paper"
    print("Computer = choose paper")
elif computerInt == 2:
    Computer = "sicssors"
    print("Computer = choose sicssors")
else:
    print("Computer = error!")

if player == Computer:
    print("Its a Draw")
elif player == "rock":
    if Computer == "paper":
        print("Computer Wins")
    else:
        print("You Win")
elif player == "paper":
    if Computer == "rock":
        print("You Win")
    else:
        print("Computer Win")
elif player == "scissiors":
    if Computer == "rock":
        print("Computer Wins")
    else:
        print("You Win")
