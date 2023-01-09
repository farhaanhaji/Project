import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = 'X'
winner = ''
gameRunning = True


# printing the game board

def Print_Board(board):
    print(board[0] + ' ' + board[1] + ' ' + board[2])
    print(board[3] + ' ' + board[4] + ' ' + board[5])
    print(board[6] + ' ' + board[7] + ' ' + board[8])


Print_Board(board)


# take player input
def PlayerInput(board):
    inp = int(input('enter a number 1-9: '))
    if 1 <= inp <= 9 and board[inp - 1] == '-':
        board[inp - 1] = currentPlayer
    else:
        print('oops player is already in that spot')


# check for win or tie
def check_horizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != board[1]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]


def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True


def check_tie(board):
    global gameRunning
    if '-' not in board:
        Print_Board(board)
        print('the game is a tie')
        gameRunning = False


def Check_win():
    if check_vertical(board) or check_horizontle(board) or check_diag(board):
        print(f'the winner is {winner}')


# switch the player

def switch_player():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = '0'
    else:
        currentPlayer = 'X'

# computer

def computer(board):
    while currentPlayer == 'O':
        position = random.randint(0, 8)
        if board[position] == '-':
            var = board[position] == 'O'
            switch_player()




# check for win or tie again

while gameRunning:
    Print_Board(board)
    PlayerInput(board)
    Check_win()
    check_tie(board)
    switch_player()
    computer(board)
    Check_win()
    check_tie(board)
