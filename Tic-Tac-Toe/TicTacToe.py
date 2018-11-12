
board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('  |   |')
    print(board[1]+' | ' +board[2]+' | ' + board[3])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(board[4]+' | ' +board[5]+' | ' + board[6])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(board[7]+' | ' +board[8]+' | ' + board[9])
    print('  |   |')
def isWinner(bo,le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

printBoard(board)
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:  #We need to make sure that our program doesn't crash if the user types an invalid input
            move = int(move)  #We check if the player typed an integer
            if move>0 and move<10: # and the possition is within these values
                if spaceIsFree(move):
                    run = False   
                    insertLetter('X',move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x != 0] #This will return all the possible moves that are available.
    move = 0

    for let in ['O','X']:  #We make a copy of the board and we check if there's a wining possition for '0' or 'X'
        for i in possibleMoves:
            boardCopy = board[:]  # we make a copy of our board, and we use [:] so that when a change occures in boardCopy it does not reflect back on the original board!! 
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move

    cornersOpen = [] #We will try to find if the corners are available, if yes, we will pick one randomly 
    for i in possibleMoves:
        if i in[1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0: 
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:  #We check if the center is available
        move = 5
        return move

    edgesOpen = [] #We will try to find if the edges are available, if yes, we will pick one randomly 
    for i in possibleMoves:
        if i in[2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0: 
        move = selectRandom(edgesOpen)

    return move    #If there's no possible moves, we still need to return something and by default, move is equal to 0


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True        

def main():
    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):  #We check if the computer won, if yes the func. will return true 
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O\'s won this time!")
            break   
        if not(isWinner(board,'X')):  #We check if the player won, if yes the func. will return true 
            move = compMove()
            if move == 0:
                print('Tie game')
            else:
                insertLetter('O',move)
                print('Computer placed an \'O\' in position',move,':')
                printBoard(board)
        else:
            print("X\'s won this time! Good job!")
            break                       

    if isBoardFull(board):
        print('Tie Game!')    

main()