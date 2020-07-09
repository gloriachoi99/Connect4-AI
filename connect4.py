# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:06:26 2020

@author: gchoi
"""

#Name: Gloria Choi (in a group with Karoline Blendstrup)

import random

def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + '\n'  # bottom of the board

        for x in range(0, self.width):
            s += ' ' + str(x) 
        # and the numbers underneath here

        return s       # the board is complete, return it
    def addMove(self, col, ox):
        """col represents index of column to which checker will
        be added; ox is a one-character string representing 
        checker to add to the board; ox should be either 'X' or 'O'
        """
        for row in range(0, self.height):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return 
        self.data[self.height-1][col] = ox

    def clear(self):
        """clears the board that calls it
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.data[row][col] = ' '

    
    def setBoard(self, moveString):
        """Sets the board according to a string
           of turns (moves), starting with 'X'.
           If show == True, it prints each one.
        """
        nextChecker = 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, col):
        """returns True is calling object does allow a move
        into column c; returns False if column c is not a 
        legal column number for the calling object and if 
        column c is full (checks to be sure that c is within
        range from 0 to last column and that there is still
        room left in the column)
        """
        W = self.width
        D = self.data
        if col < 0 or col >= W:
            return False
        elif D[0][col] != ' ':
            return False
        else:
            return True
    
    def isFull(self):
        """returns True if calling object is completely full
        of checkers and False otherwise
        """
        for col in range(0, self.width):
            for row in range(0, self.height):
                if self.data[row][col] == ' ':
                    return False
        return True

    def delMove(self, c):
        """removes the top checker from the column c; if 
        column is empty, delMove should do nothing
        """
        for row in range(0, self.height):
            if self.data[row][c] != ' ':
                self.data[row][c] = ' '
                return 

    def winsFor(self, ox):
        """ox is a 1-character checker either 'X' or 'O'
        returns True if there are four checkers of type ox
        in a row on the board
        returns False otherwise
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
                if inarow_Neast(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nsouth(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nnortheast(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nsoutheast(ox, row, col, self.data, 4) == True:
                    return True
        return False

    def hostGame(self):
        """hosts game of Connect Four; alternates turns
        between 'X' (will always go first) and 'O';
        asks the user to select a column number for each 
        move
        """
        ox = input("Please choose X or O:")
        while ox not in 'XO': 
            ox = input("That was not an option. Please choose X or O:")
        if ox == 'X':
            opponent = 'O'
        else:
            opponent = 'X' 

        while not self.isFull():
            users_col = self.aiMove(opponent)
            self.addMove(users_col, opponent)
            print(self)
            if self.winsFor(opponent) == True:
                print(opponent, 'has won the game')
                break
            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("Choose a column: "))
            self.addMove(users_col, ox)
            print(self)
            if self.winsFor(ox) == True:
                print(ox, 'has won the game')
                break
        if self.isFull():
            print('It was a tie')
    
    def colsToWin(self, ox):
        """ox is the string 'X' or 'O'
        returns the list of the columns where ox can move in
        the next turn in order to win and finish the game
        should not look ahead more than one turn
        columns should be in numeric order if there are more
        than one
        """
        L = []
        for col in range(0, self.width):
            if self.allowsMove(col):
                self.addMove(col, ox)
                if self.winsFor(ox):
                    L += [col]
                self.delMove(col)
        return L

    def aiMove(self, ox):
        """argument ox is string 'X' or 'O'
        returns a single integer, which must be a legal 
        column in which to make a move
        
        If there is a way for ox to win, then aiMove MUST 
        return that move (that column number). It must win 
        when it can. There may be more than one way to win: 
        in this case, any one of those winning column moves 
        may be returned.

        If there is NO way for ox to win, but there IS a way 
        for ox to block the opponent's four-in-a-row, then 
        aiMove MUST return a move that blocks its opponent's 
        four-in-a-row. Again, it should not look more than one 
        move ahead for its opponent. If there are no wins, but 
        multiple ways to block the opponent, then aiMove should
        return any one of those ways to block the opponent. 
        (Even though the opponent might win in a different way.)
        
        If there is NO way for ox to win NOR a way for ox to 
        block the opponent from winning, then aiMove should 
        return a move of your (the programmer's) choice—but it 
        must be a legal move. We won't call aiMove when the board
        is full.
        """
        if ox == 'X':
            opponent = 'O'
        else:
            opponent = 'X' 
        
        if self.colsToWin(ox):
            return random.choice(self.colsToWin(ox))
        elif self.colsToWin(opponent):
            return random.choice(self.colsToWin(opponent))
        else:
            return random.choice(range(0, self.height))

    def playGame(self, pForX, pForO, ss = False):
        """Plays a game of Connect Four.
            p1 and p2 are objects of type Player OR
            the string 'human'.
            If ss is True, it will "show scores" each time.
        """

        nextCheckerToMove = 'X'
        nextPlayerToMove = pForX

        while True:

            # print the current board
            print(self)

            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove(col):
                    col = int(input('Next col for ' + nextCheckerToMove + ': '))
            else: # it's a computer player
                if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((nextCheckerToMove + "'s"), 'Scores: ', [int(sc) for sc in scores])
                    print()
                    col = nextPlayerToMove.tiebreakMove(scores)
                else:
                    col = nextPlayerToMove.nextMove(self)

            # add the checker to the board
            self.addMove(col, nextCheckerToMove)

            # check if game is over
            if self.winsFor(nextCheckerToMove):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
                nextPlayerToMove = pForO
            else:
                nextCheckerToMove = 'X'
                nextPlayerToMove = pForX

        print('Come back 4 more!')


class Player:
    """An AI player for Connect Four."""

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """returns the other kind of checker (checker played
        by self's opponent)
        """
        if self.ox == 'X':
            return 'O'
        else:
            return 'X' 

    def scoreBoard(self, b):
        """returns a single float value representing the 
        score of the input b, which will be an object of 
        type Board
        returns 100.0 if board b is a win for self, 50.0 if
        neither win nor lose for self, and 0.0 if lose for self
        """
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0
            
    def tiebreakMove(self, scores):
        """scores is nonempty list of floating-point numbers
        if there is only one highest score in the scores list,
        return column number (not actual score)
        """
        maximum = max(scores)
        maxIndex = 0 
        maxIndices = []
        for i in range(len(scores)):
            if scores[i] == maximum:
                maxIndices += [maxIndex]
            maxIndex += 1
        if self.tbt == 'LEFT':
            return maxIndices[0]
        elif self.tbt == 'RIGHT':
            return maxIndices[-1]
        else:
            return random.choice(maxIndices)
    
    def scoresFor(self, b):
        """return a list of scores with the c-th score 
        representing the goodness of the input board after
        the player moves to column c
        """
        scores = [self.scoreBoard(b)]*b.width
        for i in range(len(scores)):
            if b.allowsMove(i) == False:
                scores[i] = -1.0
            elif self.ply != 0:
                b.addMove(i, self.ox)
                score = self.scoreBoard(b)
                if score == 100.0:
                    scores[i] = 100.0
                else:
                    opponent = Player(self.oppCh(), self.tbt, self.ply-1)
                    bestOpponent = max(opponent.scoresFor(b))
                    scores[i] = 100.0 - bestOpponent
                b.delMove(i)
        return scores
    
    def nextMove(self, b):
        """b is an object of type Board and returns an integer
        for the column number that the calling object (Player)
        chooses to move to
        """
        result = self.scoresFor(b)
        best = self.tiebreakMove(result)
        return best

class TetrisBoard:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + '\n'  # bottom of the board

        for x in range(0, self.width):
            s += ' ' + str(x) 
        # and the numbers underneath here

        return s       # the board is complete, return it
    def addMove(self, col, ox):
        """col represents index of column to which checker will
        be added; ox is a one-character string representing 
        checker to add to the board; ox should be either 'X' or 'O'
        """
        for row in range(0, self.height):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return 
        self.data[self.height-1][col] = ox

    def clear(self):
        """clears the board that calls it
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.data[row][col] = ' '

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'
        

    def allowsMove(self, col):
        """returns True is calling object does allow a move
        into column c; returns False if column c is not a 
        legal column number for the calling object and if 
        column c is full (checks to be sure that c is within
        range from 0 to last column and that there is still
        room left in the column)
        """
        W = self.width
        D = self.data
        if col < 0 or col >= W:
            return False
        elif D[0][col] != ' ':
            return False
        else:
            return True
    
    ###TETRIS MODE OF CONNECT FOUR (OPTION 3)######
    def BottomRowisFull(self):
        """if the row is full, delete the row and fix the board accordingly
        returns True if bottom row is full, and False otherwise
        """
        D = self.data
        W = self.width
        H = self.height
        for col in range(W):
            if D[H-1][col] == ' ':
                return False
        return True

    def BottomRowdelMove(self):
        """deletes the bottom row and shifts each row above it down one row to take the bottom row's place
        """
        if self.BottomRowisFull() == True:
            for col in range(self.width):
                self.data[self.height-1][col] = ' '
            
           
            for row in range(self.height-1, 0, -1):
                for col in range(self.width):
                    if self.data[row][col] != ' ':
                        if self.data[row][col] == 'X':
                            self.data[row + 1][col] = 'X'
                            self.data[row][col] = ' '
                        else:
                            self.data[row + 1][col] = 'O'
                            self.data[row][col] = ' ' 
                
    ########################

    def isFull(self):
        """returns True if calling object is completely full
        of checkers and False otherwise
        """
        for col in range(0, self.width):
            for row in range(0, self.height):
                if self.data[row][col] == ' ':
                    return False
        return True

    def delMove(self, c):
        """removes the top checker from the column c; if 
        column is empty, delMove should do nothing
        """
        for row in range(0, self.height):
            if self.data[row][c] != ' ':
                self.data[row][c] = ' '
                return 

    def winsFor(self, ox):
        """ox is a 1-character checker either 'X' or 'O'
        returns True if there are four checkers of type ox
        in a row on the board
        returns False otherwise
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
                if inarow_Neast(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nsouth(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nnortheast(ox, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nsoutheast(ox, row, col, self.data, 4) == True:
                    return True
        return False

    def hostGame(self):
        """Hosts a full game of Connect Four. 
        """
        print("Welcome to Connect Four!")
        print(self)

        while True:
            self.BottomRowdelMove()

            #X's turn
            turn = int(input("X's choice: "))
            
            while not self.allowsMove(turn):
                turn = int(input("Please choose a valid column number: "))

            self.addMove(turn,'X')
            print(self)

            if self.winsFor('X'):
                print("Congratulations player X has won!")
                break
            if self.isFull():
                print("It's a tie!")
                break

            self.BottomRowdelMove()
            #O's turn
            aiTurn = self.aiMove('O')
            print("Computer chooses column: ", str(aiTurn))
            
            self.addMove(aiTurn,'O')
            print(self)

            if self.winsFor('O'):
                print("The Computer won!")
                break
            if self.isFull():
                print("It's a tie!")
                break

    def colsToWin(self, ox):
        """ox is the string 'X' or 'O'
        returns the list of the columns where ox can move in
        the next turn in order to win and finish the game
        should not look ahead more than one turn
        columns should be in numeric order if there are more
        than one
        """
        L = []
        for col in range(0, self.width):
            if self.allowsMove(col):
                self.addMove(col, ox)
                if self.winsFor(ox):
                    L += [col]
                self.delMove(col)
        return L

    def aiMove(self, ox):
        """argument ox is string 'X' or 'O'
        returns a single integer, which must be a legal 
        column in which to make a move
        
        If there is a way for ox to win, then aiMove MUST 
        return that move (that column number). It must win 
        when it can. There may be more than one way to win: 
        in this case, any one of those winning column moves 
        may be returned.

        If there is NO way for ox to win, but there IS a way 
        for ox to block the opponent's four-in-a-row, then 
        aiMove MUST return a move that blocks its opponent's 
        four-in-a-row. Again, it should not look more than one 
        move ahead for its opponent. If there are no wins, but 
        multiple ways to block the opponent, then aiMove should
        return any one of those ways to block the opponent. 
        (Even though the opponent might win in a different way.)
        
        If there is NO way for ox to win NOR a way for ox to 
        block the opponent from winning, then aiMove should 
        return a move of your (the programmer's) choice—but it 
        must be a legal move. We won't call aiMove when the board
        is full.
        """
        if ox == 'X':
            opponent = 'O'
        else:
            opponent = 'X' 
        
        if self.colsToWin(ox):
            return random.choice(self.colsToWin(ox))
        elif self.colsToWin(opponent):
            return random.choice(self.colsToWin(opponent))
        else:
            return random.choice(range(0, self.height))

    def playGame(self, pForX, pForO, ss = False):
        """Plays a game of Connect Four.
            p1 and p2 are objects of type Player OR
            the string 'human'.
            If ss is True, it will "show scores" each time.
        """

        nextCheckerToMove = 'X'
        nextPlayerToMove = pForX

        while True:

            # print the current board
            print(self)

            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove(col):
                    col = int(input('Next col for ' + nextCheckerToMove + ': '))
            else: # it's a computer player
                if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((nextCheckerToMove + "'s"), 'Scores: ', [int(sc) for sc in scores])
                    print()
                    col = nextPlayerToMove.tiebreakMove(scores)
                else:
                    col = nextPlayerToMove.nextMove(self)

            # add the checker to the board
            self.addMove(col, nextCheckerToMove)

            # check if game is over
            if self.winsFor(nextCheckerToMove):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
                nextPlayerToMove = pForO
            else:
                nextCheckerToMove = 'X'
                nextPlayerToMove = pForX

        print('Come back 4 more!')