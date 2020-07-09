# Connect4-AI
This was the final project for Harvey Mudd College's CS 5 (Introduction to CS) in Spring 2018.

### About
With the help of the CS5 grutors and Professor Geoff Kuenning, my classmate, Karoline, and I created a Python program that allows a human to play Connect4 with an AI opponent. We created several methods based on what our instinctual reactions to an opponent's move would be. For example, if an opponent had three of their X's in a vertical row, the next move for the AI (and for most people) would be to block the opponent from inserting their fourth X in that row.

### Making It More Fun
In our Connect 4 game, we decided to take an extra step and delete the bottom row of the board once it 
becomes full, regardless of the pieces (X's or O's) that are in that row. We created two functions to accomplish this task- bottomRowIsFull and deleteBottomRowIfFull. 

### How To Play
When playing our game, we encourage you to use hostGame() within the TetrisBoard class (the modified class with this new rule). This will achieve our desired goal of deleting the bottom row of the board completely once it has been filled, and the corresponding rows will fall into place like gravity! 

For your reference, you can find a demo of an example game [here](demo.jpg). In this game, I have specified a 5 x 5 board. 

For those who may be unfamiliar with calling methods in a class, you can find an example of how to start the game using the command line output [here](examplecommandline.txt). When initializing the board, you must specify the width and height of the board which you wish to play on.

\
Happy playing!
