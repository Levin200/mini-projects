from tkinter import *
from tkinter import ttk
from random import *

# Create Object
root = Tk()

# Set geometry
root.geometry("1360x340")

# Set title
root.title("Rock-Paper-Scissors-Game")

# Giving a title to the game
game_title = Label(root,text="Rock-Paper-Scissors-Game",font=("arial",14),width=50,height=4)
game_title.grid(row=1,column=2)

# Initializing the game scores
player_points = 0
computer_points = 0
"""
Here the values are used which reffer
0 -> ROCK
1 -> PAPER
2 -> SCISSORS

"""
def evaluvate(user_value):
    # Computer chooses value between 0 and 2
    computer_value = randint(0,2)
    # Display computer's random selection
    hands = ["Rock","Paper","Scissors"]
    computer_choise.config(text="Computer : {}".format(hands[computer_value]))

    # declare the points global to use it outside the function
    global player_points
    global computer_points

    # If the user selects rock -> 0
    if user_value == 0:
        if computer_value == 0:
            game_bot.config(text="Tie! - "+" Computer:Bad luck")
        elif computer_value == 1:
            game_bot.config(text="YOU Loose - "+" Computer: I am better ")
            computer_points += 1
        else:
            game_bot.config(text="YOU Won - "+" Computer: You won by luck")
            player_points += 1

    # If the user selects paper -> 1
    if user_value == 1:   
        if computer_value == 1:
            game_bot.config(text="Tie! - "+" Computer:Bad luck")
        elif computer_value == 0:
            game_bot.config(text="YOU Loose - "+" Computer: I am better ")
            computer_points += 1
        else:
            game_bot.config(text="YOU Won - "+" Computer: You won by luck")
            player_points += 1

    # If the user selects scissors -> 2
    if user_value == 2:   
        if computer_value == 2:
            game_bot.config(text="Tie! - "+" Computer:Bad luck")
        elif computer_value == 1:
            game_bot.config(text="YOU Loose - "+" Computer: I am better ")
            computer_points += 1
        else:
            game_bot.config(text="YOU Won - "+" Computer: You won by luck")
            player_points += 1

    player_score.config(text ="Player Score: {}".format(player_points))
    computer_score.config(text="Computer Score = {}".format(computer_points))


computer_score = Label(root,text="Computer Score = {}".format(computer_points),font=("arial",10),width=50,height=4)
computer_score.grid(row=2,column=1,sticky='ew')

player_score = Label(root,text="Player Score: {}".format(player_points),font=("arial",10),width=50,height=4)
player_score.grid(row=2,column=3,sticky='ew')

computer_choise = Label(root,text="",font=("arial",10),width=50,height=4)
computer_choise.grid(row=3,column=2)

rock = Button(root,text="ROCK",font=("bell mt",10),command=lambda:evaluvate(0))
rock.grid(row=4,column=1,sticky='ew')

paper = Button(root,text="PAPER",command=lambda:evaluvate(1))
paper.grid(row=4,column=2,sticky='ew')

scissors = Button(root,text="SCISSORS",font=("bell mt",10),command=lambda:evaluvate(2))
scissors.grid(row=4,column=3,sticky='ew')

game_bot = Label(root,text="",font=("arial",14),width=50,height=4)
game_bot.grid(row=7,column=2)

root.mainloop()