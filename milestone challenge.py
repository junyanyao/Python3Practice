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
        marker =input('Player 1, choose X or O: ').upper()
        
    
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), 
#and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position]=marker
    



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



#Step 5: Write a function that uses the random module to randomly decide which player goes first. 
#You may want to lookup random.randint() Return a string of which player went first.

import random

def choose_first():
    x= random.randint(1,2)
    if x==1:
        return 'Player 1 goes first'
    else:
        return 'Player 2 goes first'
    


#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available
        
def space_check(board, position):
    return board[position]==' '


#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    full= 0
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
            
#Step 8: Write a function that asks for a player's next position (as a number 1-9) 
#and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    position  = 0
    while position not in [1,2,3,4,5,6,7,8,9] or (not space_check(board, position)):
        position = int(input('please choose a position : (1-9)'))
        
    return position

#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    choice = input('Play again? Please answer Yes or No')
    return choice =='Yes'


#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
    
#let player choose marker:
    

print('Welcome to the game!')

#reset the board:
while True:
    TheBoard =[' ']*10
    player1_marker, player2_marker= player_input()
    turn= choose_first()
    
    play_game =input('Are you ready? please enter yes or no ')
    if play_game =='yes':
        game_on= True
    else:
        game_on =False
    
    while game_on:
        if turn== 'player1':
            display_board(TheBoard)
            position= player_choice(TheBoard)
            place_marker(TheBoard, player1_marker, position)
        
            if win_check(TheBoard, player1_marker):
                display_board(TheBoard)
                print('Cong! You won')
                game_on =False
            else:
                if full_board_check(TheBoard):
                    print('Tie game')
                    game_on= False
                    break
                else:
                    turn = 'player2'
        else:
            display_board(TheBoard)
            position =player_choice(TheBoard)
            place_marker(TheBoard, player2_marker, position)
        
            if win_check(TheBoard, player2_marker):
                display_board(TheBoard)
                print('Cong! you Won')
                game_on= False
            else:
                if full_board_check(TheBoard):
                    print('Tie game')
                    break
                else:
                    turn= 'player1'
    if not replay():
        break
                

        
                
    
            
                
            
            
        
        
    
    
    
