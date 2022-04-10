#Notes: When making projects, think of sequence of what needs to be done
#https://www.youtube.com/watch?v=dK6gJw4-NCo&ab_channel=CodeCoach
#Set Global Variables - use to access in any functions of program.
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None  #initialize w/ no value, so can change later.
gameRunning = True
#Print Game Board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])
#Take Player Input
def playerInput(board):
    inp = int(input("Enter a number from 1-9: ")) #turn to integer to make use of indexes
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Error :/")
#Check for Win or Tie
def checkHorizontal(board):
    global winner #global states that if we change var within function, changes throughout file
    if board [0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True #so we can do if checkhorizontal True, then can break out of game loop
    elif board [3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board [6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True 

def checkVert(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie!")
        gameRunning = False

def checkWin(board):
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkVert(board):
        print(f"The winner is {winner}")
        gameRunning = False
        
#Switch Play
def switchPlayer(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O" #single equals sign to reassign
    else:
        currentPlayer = "X"

#Check for Win or Tie Again

while gameRunning:
    printBoard(board)
    playerInput(board)
    switchPlayer(board)
    checkWin(board)
    checkTie(board)
    