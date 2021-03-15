# Interactive Minigame Menu & Games"


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

def minigame_menu():
    
    choice = int(input("What game would you like to play?\n1. Coinflip\n2. Dice\n3. Magic 8ball\n4. Number Guessing game"))
    
    if choice == 1:
        coinflip()
    
    elif choice == 2:
        dice()
    
    elif choice == 3:
        eightball()
    
    elif choice == 4:
        guess()

    else:
        print("Invalid number provided!")

minigame_menu();
