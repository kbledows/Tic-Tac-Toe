#This is a tic tac toe AI by Konrad Bledowski, 6-19-2021
import time

#The main gameboard. It begins as an empty 3x3 array.
gameboard = [['.','.','.'],
			 ['.','.','.'],
			 ['.','.','.']]

#A dictionary to connect board spaces with numbers for player moves.
pos_dict = {
	"1": gameboard[0][0],
	"2": gameboard[0][1],
	"3": gameboard[0][2],
	"4": gameboard[1][0],
	"5": gameboard[1][1],
	"6": gameboard[1][2],
	"7": gameboard[2][0],
	"8": gameboard[2][1],
	"9": gameboard[2][2]
}

#Empty spot on the board (no pieces)
EMPTY = '.'

#Simple method to print the entire board.
def printboard():
	for row in gameboard:
		print(row)

#Player's move. 9 possible positions
def playerMove():
	print("Positions are as follows:")
	print("1, 2, 3")
	print("4, 5, 6")
	print("7, 8, 9")
	position = input("Please select a position.")
	position = int(position)
	#positionSpot is the real spot on the board and is calculated using the below formula.
	positionSpot = gameboard[(position - 1)//3][(position - 1) % 3]
	while positionSpot != EMPTY:
		print("Invalid positon, already marked by player or computer. please try again.")
		print("Positions are as follows:")
		print("1, 2, 3")
		print("4, 5, 6")
		print("7, 8, 9")
		position = (input("Please select a position."))
		position = int(position)
		positionSpot = gameboard[(position - 1)//3][(position - 1) % 3]
	position = int(position)
	gameboard[(position - 1)//3][(position - 1) % 3] = 'X'

#Insert Letter method used for the computer. inserts letter O in given row/column
def insertLetter(positionR,positionC):
	if isSpaceFree(positionR,positionC) == True:
		gameboard[positionR][positionC] = 'O'
	else: #Catching an error - should not occur
		print("Error: Space is not free.")
		return

def computerMove(): #Computer makes a move using minimax recursive function
	 bestScore = -1000 #best score is lowest possible value for opponent
	 bestMoveR = 0 #best possible move found using minimax
	 bestMoveC = 0
	 for i in range(3):
	 	for j in range(3):
	 		if gameboard[i][j] == EMPTY:
	 			gameboard[i][j] = 'O'
	 			score = minimax(gameboard,0,False)
	 			gameboard[i][j] = EMPTY
	 			if score > bestScore:
	 				bestScore = score 
	 				bestMoveR = i
	 				bestMoveC = j
	 insertLetter(bestMoveR,bestMoveC)
	 return

def minimax(board,depth,isMaximizing):
	if winCondition(board) == (True,'O'): #Computer has won
		return 1
	elif winCondition(board) == (True,'X'): #Player has won
		return -1
	elif checkFull(): #A Tie has occured
		return 0

	if isMaximizing: #computer playing for itself (maximizing)
		bestScore = -1000 #temporary value, (anything greater than -1000)
		for i in range(3):
			for j in range(3):
				if board[i][j] == EMPTY:
					board[i][j] = 'O'
					score = minimax(board,0,False)
					board[i][j] = EMPTY
					if (score > bestScore):
						bestScore = score
		return bestScore

	else: #computer playing for opponent (minimizing damage)
		bestScore = 1000 #temporary value (anything is less than 1000)
		for i in range(3):
			for j in range(3):
				if board[i][j] == EMPTY:
					board[i][j] = 'X'
					score = minimax(board,depth+1,True)
					board[i][j] = EMPTY
					if score < bestScore:
						bestScore = score
		return bestScore


def isSpaceFree(positionR,positionC):
	if gameboard[positionR][positionC] == EMPTY:
		return True
	else:
		return False

def checkFull():
	for i in range (3):
		for j in range(3):
			if gameboard[i][j] == EMPTY:
				return False
	return True


def winCondition(board):
	win = False
	team = None
	for row in board:
		if row[0] == row[1] == row[2] != EMPTY:
			return True, row[0]
	for i in range(3):
		if board[0][i] == board[1][i] == board[2][i] != EMPTY:
			return True, board[0][i]
	if board[0][0] == board[1][1] == board[2][2] != EMPTY:
		return True, board[0][0]
	if board[0][2] == board[1][1] == board[2][0] != EMPTY:
		return True, board[0][2]

	return False, None


def main():
	boardFull = False
	wC = False
	print("Welcome to Tic Tac Toe")
	time.sleep(0.5)
	printboard()
	print("Above is the beginning board state.")
	time.sleep(0.5)
	print("Player == [ X ]")
	time.sleep(0.5)
	print("Computer == [ O ]")
	print("The computer ( O ) moves first.")
	while winCondition(gameboard)[0] == False:
		if checkFull() == True:
			break
		computerMove()
		print("Computer is thinking...")
		printboard()
		#wC = (winCondition(gameboard)[0])
		print("The computer has chosen the above move.")
		if checkFull() == True:
			break
		playerMove()
		printboard()
		boardFull = checkFull()

	if wC == True:
		if winCondition(gameboard)[1]  == "X":
			print("Player has won :)")
			return
		else:
			print("AI has won :(")
	else:
		print("It's a Tie!")

main()