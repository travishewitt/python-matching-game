from random import choice



#ok, we gonna make a matching game
#it's gonna have a grid of objects, q r s t u
#we gonna make this grid 8x8
#mechanics: objects'll disappear by matching three or more in a row or column.
#   swaps with adjacent pieces only. when three or more are matched, the remaining objects will then rearrange


#basic steps:
#1: initialize and setup
#2: loop, make sure it's not time to end the game
#3: in the loop, go through one round of the game


################################################################################
################################################################################
                      ### MY SEXY FUNCTION GARDEN ###

def InitializeGrid(board):
    #We gonna initialize grid by reading in from a file.
    print("Initializing grid!")
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(["Q", "R", "S", "T", 'U'])

def Initialize(board):
    #Initializes the game and board.
        #Initialize game
        #Initialize grid
    InitializeGrid(board)
        #Initialize score
    global score
    score = 0
        #Initialize turn
    global turn
    turn = 0

    print("Initializing, sweetie-pie.")

def DrawBoard(board):
    #Display board to screen
    print("Drawing up the board, cuteness")
    linetodraw = ""
    #Draw some blank lines first
    print("\n\n\n")
    print("---------------------------------------")
    #Now draw rows from 8 to 1
    for i in range(7, -1, -1):
        #Draw each row
        linetodraw=""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print("---------------------------------------")
    print("   a   b   c   d   e   f   g   h")
    global score
    print("Current score: ", score)

def IsValid(move):
    #returns true if valid, false if not
    if len(move) != 3:
        return False
    if not (move[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        return False
    if not (move[1] in ['1', '2', '3', '4', '5', '6', '7', '8']):
        return False
    if not (move[2] in ['u', 'd', 'l', 'r']):
        return False
    #check to see if the first column moves are not left

    if (move[0] == 'a') and (move[2] == 'l'):
        return False
    #check to see that the last column does not move right
    if (move[0] == 'h') and (move[2] == 'r'):
        return False
    #the bottom row cannot move down
    if (move[1] == '1') and (move[2] == 'd'):
        return False
    #the top row cannot move up
    if (move[1] == '8') and (move[2] == 'u'):
        return False
    return True

def GetMove():
    print("Enter a move by specifying a space and direction. (u, d, l, r). Spaces should list column, then row.")
    print("For Example: e3u will swap position e3 with the piece above it. f7r would swap position f7 and the piece to the right of it.")
    move = input("Enter move: ")
    return move

def ConvertLetterToCol(Col):
    if Col == 'a':
        return 0
    elif Col == 'b':
        return 1
    elif Col == 'c':
        return 2
    elif Col == 'd':
        return 3
    elif Col == 'e':
        return 4
    elif Col == 'f':
        return 5
    elif Col == 'g':
        return 6
    elif Col == 'h':
        return 7
    else:
        return -1


def SwapPieces (board, move):
    print("Swapping pieces")
    #Swap pieces on board
    #Get original position

    origrow = int(move[1]) - 1
    origcol = ConvertLetterToCol(move[0])

    #Get adjacent position
    if (move[2]) == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif (move[2]) == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif (move[2]) == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif (move[2]) == 'r':
        newrow = origrow
        newcol = origcol + 1

    #Swap objects in two positions

    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp

def RemovePieces (board):
    #gonna generate another board to track whether pieces should be removed or not
    #initialize this board copy to "not"
    remove = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]
    #go through each row looking for three in a row of the same
        #if found, mark them for removal
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
                remove[i][j] = 1;
                remove[i][j+1] = 1;
                remove[i][j+2] = 1;
    #go through each column looking for three in a row of the same
        #if found, mark them for removal
    for j in range(8):
        for i in range(6):
            if (board [i][j] == board[i+1][j] and board[i][j] == board[i+2][j]):
                remove[i][j] = 1;
                remove[i+1][j] = 1;
                remove[i+2][j] = 1;
    #eliminate marked pieces
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any

    print("Removing pieces")
    return False

def DropPieces (board):
    #Gravity happens, if u know what I'm sayin
    print("Dropping pieces")
    #make a list of pieces in the column
    for j in range(8):
        listofpieces = []
        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
            #then we copy that list into the column
        for i in range(len(listofpieces), 8):
            board[i][j] = 0


def FillBlanks (board):
    #Filling blank pieces with new random objects
    print("Filling blanx")
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(["Q", "R", "S", "T", 'U'])

def UpdateBoard(board, move):
    print("Updating board")
    #According to move, update the board
    #Swap pieces according to move
    SwapPieces(board, move)
    pieces_eliminated = True
    #Repeat until no eliminations occur
        #Remove pieces 3 in a row or 3 in a column
    while pieces_eliminated:
        pieces_eliminated = RemovePieces(board)
        #Drop remaining objects down
        DropPieces(board)
        #Fill in blanks with new random objects
        FillBlanks(board)

def ContinueGame(current_score, goal_score = 100):
    #Returns a boolean. If false, game will end, if true, game will continue.
    #If score is greater than goal score, return False. Otherwise, it'll be true
    print("Checking to see if we should continue, sweet baby-pie o' mine.")
    if (current_score >= goal_score):
        return False
    else:
        return True

def DoRound(board):
    print("Doing a round, baby")
    #Does a round of the game. duh.
    #Displays current board
    DrawBoard(board)
    #Gets move
    move = GetMove()
    #Updates Board
    UpdateBoard(board, move)
    #Update turn number
    global turn
    turn += 1





################################################################################
################################################################################

                        ### MY MAIN VARIABLEZ ###

score = 0
turn = 0
goal_score = 100

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

################################################################################
################################################################################

                        ### MY MAIN PRGRAM ###

################################################################################
################################################################################

#Initialize
    #We gonna set up the grid itself
    #We gonna set the user's score to 0
    #We gonna set up other variables we need, like, which round we are on, etc.
    #We'll pass in some variables as parameters, and also establish global variables, since we'll need them everywhere
Initialize(board)

#Loop while game is not over
while ContinueGame(score, goal_score):
    DoRound(board)
    # Do a round of the game
    # One round will look like this:
    # Listen for the move (get input from user)
    # React to the move (update grid)
    # Display updated grid