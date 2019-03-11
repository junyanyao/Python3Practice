#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:56:20 2019

@author: YaoJunyan
"""

'''
Milestone Project 1
Congratulations on making it to your first milestone!
You've already learned a ton and are ready to work on a real project.

Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.

There are 4 Jupyter Notebooks related to this assignment:

This Assignment Notebook
A "Walkthrough Steps Workbook" Notebook
A "Complete Walkthrough Solution" Notebook
An "Advanced Solution" Notebook
I encourage you to just try to start the project on your own without referencing any of the notebooks. If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps. If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!

There are parts of this that will be a struggle...and that is good! I have complete faith that if you have made it this far through the course you have all the tools and knowledge to tackle this project. Remember, it's totally open book, so take your time, do a little research, and remember:
'''

'''
Milestone Project 1: Walkthrough Steps Workbook
Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

Some suggested tools before you get started:
To take input from a user:

player1 = input("Please pick a marker 'X' or 'O'")

Note that input() takes in a string. If you need an integer value, use

position = int(input('Please enter a number'))


To clear the screen between moves:

from IPython.display import clear_output
clear_output()

Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:

print('\n'*100)

This scrolls the previous board up out of view. Now on to the program!
'''
#Step 1: Write a function that can print out a board. Set up your board as a list, w
#here each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.


from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    print(board[7]+'|'+board[8] +'|'+board[9])
    print('-'+'|'+'-'+'|')
    print(board[4]+'|'+board[5] +'|'+board[6])
    print('-'+'|'+'-'+'|')
    print(board[1]+'|'+board[2] +'|'+board[3])
    

#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
#Think about using while loops to continually ask until you get a correct answer.

def player_input():
    marker= ''
    while marker != 'X' and marker !='O':
        marker =input('Player 1, choose X or O: ')
        
    player1= marker
    if player1=='X':
        player2 ='O'
    else:
        player2='X'
    return (player1, player2)

#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), 
#and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position]=marker
    

place_marker(test_board,'$',8)
display_board(test_board)

#Step 4: Write a function that takes in a board and checks to see if someone has won.

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

win_check(test_board,'X')