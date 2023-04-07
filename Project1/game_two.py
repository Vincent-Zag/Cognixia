#Adriel Zagala
#4/6/2023

import score

import random
import math

def comp_val():
    return random.randint(1,3)-1 # 1 rock, 2 paper, 3 scissor

def main():
    over = 0
    while (over != 1):
        over = game()
    #game will keep running until user wants to end the game
    
def game():
    board = [0,0,0]
    selection = ['r','p','s']
    end,valid = False,False

    prompt()#displays prompt
    first_to = int(input("First to 3 or 5: "))#will ask for the 
    print()
    while (end != True):
        p1 = input("Player 1: r, p, or s => ").lower()
        while ((p1 not in selection)):
            print("Invalid input only use r,p or s")
            p1 = input("Player 1: r,p, or s => ").lower()
        p2 = selection[comp_val()]
        board = compare(p1,p2,board)
        if board[0] == first_to:
            print("You WON")
            score.export_(board, 2)
            end = True
        elif board[1] == first_to:
            print("You LOST")
            score.export_(board, 2)
            end = True
        
        print("Score: Player1: "+str(board[0])+" Player2: "+str(board[1])+" Draws: "+str(board[2]))

    again = input(("Play again? y or n"))
    if again == 'y':
        return 0
    else:
        return 1

#returns the tuple with values added to them depeding on the generated value and user selected choice
def compare(p1,p2,score):
    if ((p1 == "p")and(p2 == "r"))or((p1 == "r")and(p2 == "s"))or((p1 == "s")and(p2 == "p")):
        score[0] += 1
    elif((p2 == "p")and(p1 == "r"))or((p2 == "r")and(p1 == "s"))or((p2 == "s")and(p1 == "p")):
        score[1] += 1
    else:
        score[2] += 1
    return score
 
def prompt():
    print()
    print("Welcome to the Rock, Paper, Scissor Game!")
    print("You will be against a computer!")
    print("Good Luck!")
    print()