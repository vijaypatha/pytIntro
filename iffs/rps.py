import random;
player = input("Choose")
player = player.lower()
print ("your choice:" + player)

computerChoice = random.randint(0,2)
if computerChoice == 0:
    computer = "rock"
    print("computer choose:Rock")
elif computerChoice == 1:
    computer = "paper"
    print("computer choose:Paper")
elif computerChoice == 2:
    computer = "sicssors"
    print("computer choose:sicssors")

if player == computer:
    print("You are tied")
elif player == "rock" and computer == "paper":
    print("computer wins")
elif player == "paper" and computer == "rock":
    print("You win")
elif player == "paper" and computer == "sicssors":
    print("You wins")
elif player == "sicssors" and computer == "paper":
        print("You wins")
elif player == "sicssors" and computer == "rock":
        print("Computer wins")
elif player == "rock" and computer == "sicssors":
        print("You wins")
