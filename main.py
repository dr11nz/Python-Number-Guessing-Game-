import sys
import random 
import math 

print("Welcome To Guess The Number Game")

x = input(('How High do you want the guessing Number to be?: '))

highNum = int(x)

if highNum < 15:
    print("You cant input a number lower than 15")
    sys.exit()

randomNum = random.randint(1, highNum)

def guess1(): 
    g1 = input("Please Enter The First Guess: ")
    gs1 = int(g1)
    if gs1 == randomNum:
        print("You Won!")
        sys.exit()
    else:
        lifes = 2
        print(f"Your Guess Was Wrong, You Have {lifes} Lifes Remaning.")
guess1()

def guess2():
    g2 = input("Please Enter The Second Guess: ")
    gs2 = int(g2)
    if gs2 == randomNum:
        print("You won!")
        sys.exit()
    else:
        lives = 1
        print(f"Your Guess Was Wrong, You Have Only {lives} Life Left")

guess2()

def guess3():
    g2 = input("Please Enter The Last Guess: ")
    gs2 = int(g2)
    if gs2 == randomNum:
        print(f"You won! The Number was {randomNum}")
        sys.exit()
    else:
        lifes = 0 
        print(f"You Lost. The Number was {randomNum}")

    while lifes == 0 == True:
        sys.exit() 

guess3()


      
