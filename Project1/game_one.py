#Adriel Zagala
#Number Guessing Game
import score

import random
import math


"""
Difficulty is set by the user ranging from 0 - 10,50,100, and 1000
"""
def set_diff():
    valid = False

    #Error exeption when a value taht is not in the range is inputted
    while (valid != True):
        try:
            npt = int(input("Select Difficulty: "))
            if (npt < 1 or npt > 4):
                raise ValueError("Invalid Entry")
        except ValueError:
            print("Invalid Entry")
        else:
            valid = True

        #Depending on the difficulty a section with assign the range value
    match npt:
        case 1:
            print("Difficulty set to Easy.")
            range_ = 10
        case 2: 
            print("Difficulty set to Medium.")
            range_ = 50
        case 3:
            print("Difficulty set to Hard.")
            range_ = 100
        case 4:
            print("Difficulty set to Impossible.")
            range_ = 1000

    return range_ #returns the range depending on the difficulty set



"""
hot_cold function will give off hints depedning 
on the input provided by the user

"""
def hot_cold(guess,comp): 
    if abs(guess - comp) == 0:
        print("NICE!!")
        return 1
    elif abs(guess - comp) <= 2:
        print("YOU'RE ON FIRE")
        return 0
    elif abs(guess - comp) <= 5:
        print("You're getting Hot")
        return 0
    elif abs(guess - comp) <= 7:
        print("You're getting Warmer")
        return 0
    elif abs(guess - comp) <= 10:
        print("Brrr. its still Chilly out")
        return 0    
    elif abs(guess - comp) >= 100:
        print("Eh. You're Freezing")
        return 0
    else:
        print("Are you even trying?")
        return 0

"""
a loop will check for the error input and then call upon the hot cold function
and if it returns the right value guessed 
it will end the loop and return the number of times the user has guessed
"""
def game(npt):
    comp = random.randint(0,npt)
    counter,over = 0,0
    game_over, valid = False, False

    while(over != 1):
        while (valid != True):
            try:
                user = int(input(f"Input Guess with the range 0 to {npt}: "))
                if (user < 0 or user > npt):
                    raise ValueError("Not in the Range! ")
            except ValueError:
                print("Invalid Entry")
            else:
                valid = True

        over = hot_cold(user,comp)
        counter += 1    
        if over == 0:
            valid = False

        #print(comp) #check value
        
    return counter
        

#displays prompt
def message():
    print()
    print("Welcome to the Number Guessing Game!")
    print("The Computer will select a number depending on the difficulty!")
    print("Guess the Number with the least number of guesses!")
    print()
    print("Select Difficulty.")
    print("1: Easy 0-10")
    print("2: Medium 0-50")
    print("3: Hard 0-100")
    print("4: Impossible 0-1000")
    print()


def main():
    message() #calls the message prompt move to have a cleaner look
    diff = set_diff() #calls diffulty setter function
    score_ = game(diff) #Game function is called with the difficulty in mind

    print()
    print(f"{score_} Tries!")
    score.export_(score_, 1)


