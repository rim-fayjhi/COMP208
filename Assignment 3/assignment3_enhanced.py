"""
@author: Rim
"""

import numpy
import random
import sys
import math


while True:         #While loop so the question keeps being asked until there is a valid answer
    try:
        board_size = int(input('Please enter the desired dimention for your tic tac toe game: '))       #The input is transformed into an integer so math operations can be done to it later on
        if board_size > 2 :     #Minimum of 3x3
            print(' ')
            break
        else:
            print(' ')
            print('Please enter a whole number of 3 or greater.')
    except ValueError:  #If the user inputs a str or a float, this avoids a crash
        print(' ')
        print(('Please enter a whole number.'))
    
number_of_cells = ((board_size**2)+1)


board = [(str(x)+' ')[0:2] for x in range(number_of_cells)]      # I am taking the first two characters using [0:2] so the grid doesn't get shifted #Filling the board with blank spaces
 

def insertBoard(letter, i):      #Here the letter is either X or O
    if i != None:
        global board     #Board is set as a global variable because I will use it in the other functions 
        board[i] = letter
    
   
def displayBoard():         #My board is the numpy array
    numpy_horizontal = (numpy.reshape(numpy.array(board[1:]),(board_size, board_size)))
    for line in numpy_horizontal:       #To be displayed, the 'quotations' around my values are removed using .join once I transform my array into a python list
        print('   '.join(numpy.ndarray.tolist(line)))
        print(' ')
   

 
 
def checkIfLegal(i):          #This checks if the space is free, if it is, then the move is legal and the player or the computer can choose that space.
    return board[i] != 'X ' and board[i] != 'O '        #If it's not 'X ' or 'O ' then it's free
 
 
 
def checkWinner(board, number):     #This returns either true or false, if any of these is true, then there is a winner.

    numpy_horizontal = (numpy.reshape(numpy.array(board[1:]),(board_size, board_size)))         #This separates my array into board_size by 1 arrays, so it seperates them horizontally
    numpy_vertical = numpy.rot90(numpy.reshape(numpy.array(board[1:]),(board_size, board_size)))        #This separates my array into 1 by board_size arrays, so it seperates them vertically
    numpy_diagonal_1 = numpy.diagonal(numpy_horizontal)         #This turns my diagonals into an array
    numpy_diagonal_2 = numpy.diagonal(numpy_vertical)    

    for line in numpy_horizontal:
        if numpy.all(line == number):        #If all of my line is 'X ' that means there is a winner, .all checks each items in the array
            return True
    
    for line in numpy_vertical:         #I am using a for loop as I have multiple horizontal or vertical lines
        if numpy.all(line == number):
            return True

    if numpy.all(numpy_diagonal_1 == number):  #Only using an if statement because I can only have 2 diagonals, no matter the size of the board
        return True
        
    if numpy.all(numpy_diagonal_2 == number):
        return True
    return False
        

 
def playerMove():       #This is the function that takes care of the user's moves
    run = True 
    while run:
        move = input('Which cell would you like to occupy: ')
        print(' ')
        try:
            move  = int(move)
            if move > 0 and move < number_of_cells:
                if checkIfLegal(move):
                    run = False      #If there is no more free cells, the game returns false so the while loop stops
                    insertBoard('X ', move)       #The user is represented by 'X '
                else:
                    print(' ')      #If there are other free slots, but the one the user chose isn't, he or she is told to select another one
                    print('This postion is already occupied!')
            else:
                print(' ')       #If the cell isn't occupied, the board isn't full but the integer isn't in range, the user is told so
                print('Please type a number within the range!') 
        except:         #This makes sure the game doesn't crash when the player doesn't input a valid number
            print(' ')
            print('Please type a number!') 
       
 
    
def randomSelection(my_list):
    if len(my_list) > 0:        #If the list has more than 0 items
        list_size = len(my_list)
        r = random.randrange(0, list_size)      #A random number is chosen
        return my_list[r]        #The random number decides the item chosen as it represents its index in the list
   
    
   
def computerMove(board):    #This function randomly selects a free cell for the computer to move in
    legal_moves = [x for x, letter in enumerate(board) if checkIfLegal(x) and x != 0] 
    move = 0            
    possible_moves = []     #Creating an empty dictionnary
    
    for letter in ['O ', 'X ']:         #This is the dummy random robot
        for i in legal_moves:
            legal_moves.append(i)   
    if len(possible_moves) > 0:   #As long as the robot has moves left, it chooses randomly within those
            move = randomSelection(possible_moves)
            return move
            
    
    
def smartComputerMove():
    
    numpy_horizontal = (numpy.reshape(numpy.array(board[1:]),(board_size, board_size)))      #This separates my array into board_size by 1 arrays, so it seperates them horizontally
    numpy_vertical = numpy.rot90(numpy.reshape(numpy.array(board[1:]),(board_size, board_size)))        #This separates my array into 1 by board_size arrays, so it seperates them vertically
    #I am transforming my edges into lists
    horizontal_edges_1 = numpy.ndarray.tolist(numpy_horizontal[0])          #This is my first horizontal row 
    horizontal_edges_2 = numpy.ndarray.tolist(numpy_horizontal[board_size-1])       #This is my last horizontal row 
    
    vertical_edges_1 = numpy.ndarray.tolist(numpy_vertical[0])          #This is my first vertical row 
    vertical_edges_2 = numpy.ndarray.tolist(numpy_vertical[board_size-1])       #This is my first vertical row 
    
    all_edges = vertical_edges_1 + vertical_edges_2 + horizontal_edges_1 + horizontal_edges_2       #The items in this list are my edges
    
    legal_moves = [x for x, letter in enumerate(board) if checkIfLegal(x) and x != 0]       #Checking legal moves
    
    legal_moves_str= [] #Empty list
    for free in legal_moves:        #Only the free edges are considered when looking for possible computer moves
        legal_moves_str.append(str(free))       #The possible moves are added to a list for the randomizer
        
    move = 0
   
    for let in ['O ','X ']:       #This verified if the computer or the player can win
        for i in legal_moves:       #We look at every empty space we have
            board_copy = board[:]        #This is a clone of my board, I put the : so that each time I modify the copy of the board, I don't actually modify the real one too.
            board_copy[i] = let         #This checks out each index and places the letter in that position
            if checkWinner(board_copy, let):        #We check if where we just placed our letter is a winner move
                move = i
                return move         #If it is, then that's the move we do.
 
 

    open_corners = []       #Creating the empty dictionary
    #This step randomly chooses an open corner for the computer to choose from.
    for i in legal_moves:        #If any of the corners are free, they are added to the dictionnary
        if i in [1, (board_size), ((board_size**2)-(board_size-1)), (board_size**2)]:         #These are the board's corners
            open_corners.append(i)
            
    if len(open_corners) > 0:       #Randomly selecting a corner if there is more than 1
        move = randomSelection(open_corners)
        return move
   
    #If the corners are not free, the computer looks at the center slot.
    
    if board_size % 2 != 0:      #There is no center when a board is of even size
        if math.ceil((board_size**2)/2) in legal_moves:         #Rounding it to the highest number, that's how the middle is found
            move = math.ceil((board_size**2)/2)
            return move

    #This step randomly chooses an open edge for the computer to choose from.
    
    open_edges = list((set(all_edges)).intersection(set(legal_moves_str)))
    
    #If any of the edges are free, they are added to the dictionnary
    
    #These are the board's edges that are not occupied yet
            
    if len(open_edges) > 0:         #Randomly selecting an edge cell if there is more than 1
        move = randomSelection(open_edges)
        
    else:
        move = randomSelection(legal_moves)
        
    #If none of these are free, we return zero and do a random move
 
    if move == None:
        move = 0
    return int(move)
 
    
 
def isBoardFull(board):  #Lets us know when the board is full, meaning there are no empty spaces left
    number_x = 0        #Initialising 
    number_o = 0
    number_x = board.count('X ')
    number_o = board.count('O ')
    number_total = number_x + number_o
    if number_total == (board_size**2):         #That only happens when the board is full
        return True
    else:
        return False
 


def main():
    #Main game loop
    print('Hello and welcome to the Tic-Tac-Toe Comp 208 challenge: Player against Computer.')
    print(' ')
    print('The board is numbered from 1 to', (number_of_cells-1) ,'as per the following:')
    print(' ')
    displayBoard()      #This shows the user what the initial board looks like
    print(' ')
    print("Player starts first. Simply input the number of the cell you want to occupy. Player’s move is marked with X. Computer’s move is marked with O.")
    
    while True: #A while loop is used so the question is asked again when the user inputs something other thatn Y or N
        answer = input('Start? (Y/N): ')
        if answer.lower() == 'y' or answer.lower() == 'n':
            if answer.lower() == 'y' :    #If the user types Y, the game proceeds
                print(' ') 
                break
            
            elif answer.lower() == 'n' :
                sys.exit()       #Exits the program once the user inputs N
                
        else: 
            print('Please write "y" or "n", do you want to start? (Y/N)') #The user is given another chance to enter their answer if they write something other than Y/N
            #I want it to restart if the user inputs something wrong
    
    while not(isBoardFull(board)):      #As long as the board isn't full this goes on
        if not(checkWinner(board, 'O ')):    #If the 'O ' satifies the winner function, then the computer wins
            playerMove()
            displayBoard()
        else:
            print(' ')
            print('Computer Wins!')
            sys.exit()
            break
 
       
        if not(checkWinner(board, 'X ')):     #If the 'X ' satifies the winner function, then the player wins
            move = smartComputerMove()      #I am doing this because my function returns something
            if move == 0:           #If the computer can't move, it's a tie
                print(' ')
                print('The game is tied.')
                sys.exit()          #The program closes once there is a winner, as requested by the assignment instructions
            else:
                insertBoard('O ', move)
                print(' ')
                print('Computer placed an O in position', move)
                print(' ')
                displayBoard()
        else:
            print(' ')
            print('Congratulations. Player Wins.')
            sys.exit()      #The program closes once there is a winner, as requested by the assignment instructions
            break
 
 
    if isBoardFull(board):
        print(' ')
        print('The game is tied.')       #If the board is full before any winner has been announced, the game is a tie.
 
    
main()