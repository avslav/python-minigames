import random


def coinflip():
    num = random.randint(1,2)

    if num == 1:
        print("You Got: Heads!")
    else:
        print("You Got: Tails!")

def dice():
    num = random.randint(1,6)

    print(f"You Rolled: {num}!")

def eightball():

    responses = ["Yes!", "No!", "Maybe!", "It is very likely!", "Cannot hear you!", "Ask again later, cannot say now", "Too early to predict!", "Absolutely not!"]

    input("What is your question?")

    response = random.choice(responses)

    print(response)

def guess():
    
    num = random.randint(1, 10)

    user = int(input("Please type a number between 1 and 10!"))

    if user == num:
        print("Correct! You guessed the number right!")
    
    else:
        print(f"Wrong! The correct number was {num}!")

def rps():

    choice = input("\nChoose rock (r), paper (p) or scissors (s)!")

    ai = ["Rock", "Paper", "Scissors"]

    aiChoice = random.choice(ai)

    if choice == "r" and aiChoice == "Rock":
        print("\nIt's a tie! We both chose rock!\n")
    
    elif choice == "p" and aiChoice == "Rock":
        print("\nRock! You win.\n")

    elif choice == "s" and aiChoice == "Rock":
        print("\nRock! You lose!\n")
    
    elif choice == "p" and aiChoice == "Paper":
        print("\nTie! We both chose paper!\n")

    elif choice == "r" and aiChoice == "Paper":
        print("\nPaper! You lose.\n")
    
    elif choice == "s" and aiChoice == "Paper":
        print("\nPaper! You win.\n")
    
    elif choice == "r" and aiChoice == "Scissors":
        print("\nScissors! You win.\n")
    
    elif choice == "p" and aiChoice == "Scissors":
        print("\nScissors! You lose.\n")
    
    elif choice == "s" and aiChoice == "Scissors":
        print("\nScissors! It's a tie!\n")
    
    else:
        print("Hmm... Something went wrong!")

def minigame_menu():
    
    choice = int(input("What game would you like to play?\n1. Coinflip\n2. Dice\n3. Magic 8ball\n4. Number Guessing game\n5. Rock, Paper, Scissors"))
    
    if choice == 1:
        coinflip()
    
    elif choice == 2:
        dice()
    
    elif choice == 3:
        eightball()
    
    elif choice == 4:
        guess()
    
    elif choice == 5:
        rps()

    else:
        print("Invalid number provided!")

minigame_menu();
