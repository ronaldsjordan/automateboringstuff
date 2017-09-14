theBoard = {'top-L': 'X', 'top-M': ' ', 'top-R': 'X',
            'mid-L': ' ', 'mid-M': 'O', 'mid-R': 'O',
            'low-L': 'O', 'low-M': 'X', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('- + - + -')
    print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('- + - + -')
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])

def gotWinner(board, turn):
    win = False
    tops = ['top-L', 'top-M', 'top-R']
    mids = ['mid-L', 'mid-M', 'mid-R']
    lows = ['low-L', 'low-M', 'low-R']
    for i in tops:
        if board[i] != turn:
            break
        else:
            win = True
    return True

turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Player ' + turn + '. Make your move.')
    while True:
        move = input()
        if theBoard[move] != ' ':
            print('Space already occupied. Select another space.')
        else:
            theBoard[move] = turn
            break
    if gotWinner(theBoard, turn):
        print(turn + ' is the winner!')
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
# print(theBoard.values('X'))