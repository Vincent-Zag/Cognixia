#Adriel Zagala
#Score Posted

def export_(value,game):
    
    name = input("Enter your Name: ")
    f = open("scoreboard.txt","a+")
    print("Score has been posted in the leaderboards!")
    #will input the name and then write the name and core into a .txt file

    match game:
        case 1:
            f.write(f"Game: Number Guessing Game! Name: {name} Tries: {value}" + '\n')
    
        case 2:
            f.write(f"Game: Rock, Paper, Scissor Game! Name: {name} Score against Computer: {value}" + '\n')
    f.close()

