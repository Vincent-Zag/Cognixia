#Adriel Zagala
#4/6/2023

import game_one #imported modules created
import game_two

def main():
    prompt()
    valid = False
    again = ""
    while (valid != True):
        try:
            npt = int(input("Game: "))
            if (npt < 1 or npt > 4):
                raise ValueError("Invalid Entry")
        except ValueError:
            print("Invalid Entry")
        else:
            valid = True
            #will check the matching game selected from 1-4
            match npt:
                case 1:
                    game_one.main()#calls the game one module
                case 2:
                    game_two.main()#calls the game two module
                case 3:
                    print("game is not released yet.")
                    valid = False

        
def prompt():
    print("What Game did you want to play? ")
    print("1: Number Guessing Game ")
    print("2: Rock, Paper, Scissor Game!")
    print("3: TBD                  ")

main()


