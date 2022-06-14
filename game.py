import random

def IsValidInput(input):
    return input == "rock" or input == "paper" or input == "scissors"

def Check(u, c):
    if u == c: print("TIE")
    elif u == "rock":
        if c == "paper": print("LOSE")
        else: print("WIN")
    elif u == "paper":
        if c == "scissors": print("LOSE")
        else: print("WIN")
    elif c == "paper": # scissors
        print("WIN")
    else:
        print("LOSE")

user = input("rock, paper or scissors? ")
if not IsValidInput(user): print("Invalid input")
cpu = random.choice(["rock", "paper", "scissors"])
print("CPU: " + cpu)
Check(user, cpu)


