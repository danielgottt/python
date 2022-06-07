import numpy as np
import random

ROW_COUNT = 6
COLUMN_COUNT = 7

#Defines the board size
def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

#Flips the board so numpy does start from top to bottom
def print_board(board):
	print(np.flip(board, 0))
	
#Sets the inputed position to the piece
def drop_piece(board, row, col, piece): 
	board[row][col] = piece
	
#This ensures the board has an empty position in the row
def valid_location(board, col): 
	return board[5][col] == 0

#Finds the first open row from the selected column and places the piece
def open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r
		
#This ensures the game can find a winning move
def win_variables(board,piece):
	# Horizontal positive and negative win check
	for c in range(COLUMN_COUNT-3):
		for r in range(6):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Vertical positive and negative win check
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Positive sloping win check
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Negative sloping win check
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

board = create_board()
print_board(board)
game_over = False
turn = 0

print ("Welcome to my Connect 4 game!")
print ("Human player moves = 1")
print ("Bot moves = 2")
print ("Human player goes first!")

while not game_over:

	if turn == 0:
		selection = int(input("Human Player, select your position! (0-6)"))
		while (selection) > 6 or (selection) < 0: #This is to verify the number picked by the human is within 0-6
			print ("Column must be in range of 0-6, select another number!")
			selection = int(input("Human player must pick another number! (0-6)"))
		if valid_location(board, selection):
			row = open_row(board, selection)
			drop_piece(board, row, selection, 1)
			if win_variables(board, 1):
				print("YOU HAVE MADE AMERICA PROUD SOLIDER, KEEP FIGHTING!")
				game_over = True

	else:
		selection = int(random.randint(0, 6))
		if valid_location(board, selection):
			row = open_row(board, selection)
			drop_piece(board, row, selection, 2)
			if win_variables(board, 2):
				print("HOW COULD YOU LET A BOT WIN! TRY AGAIN SOLDIER!")
				game_over = True

	print_board(board)
	
#The operator % (modulos) means diving 2 integers and the remainder will be returned to the loop
	turn += 1
	turn = turn % 2