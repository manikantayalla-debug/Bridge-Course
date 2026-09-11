import random

choices = ["rock", "paper", "scissor"]
userInput = input("Enter your choice (rock, paper, or scissor): ")
userInput = userInput.lower()
if not userInput in choices:
    print("Invalid choice")
    exit()

random_choice = random.choice(choices)

if userInput == random_choice:
    print("DRAW!")
    exit()
elif userInput == "rock":
    if random_choice == "paper":
        print("Bot choose Paper!")
        print("You LOST!")
    elif random_choice == "scissor":
        print("Bot choose Scissor!")
        print("You WON!")
elif userInput == "paper":
    if random_choice == "rock":
        print("Bot choose Rock!")
        print("You WON!")
    elif random_choice == "scissor":
        print("Bot choose Scissor!")
        print("You LOST!")
elif userInput == "scissor":
    if random_choice == "paper":
        print("Bot choose Paper!")
        print("You WON!")
    elif random_choice == "rock":
        print("Bot choose Rock!")
        print("You LOST!")




