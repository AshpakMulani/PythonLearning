from os import system

current_player = 2
p1_input_style = 'x'
p2_input_style = '0'

def print_board(board):
    '''
    DOCSTRING: This function takes list as argument and print it in grid
    x | x | 0
    ---------
    0 | 0 | x
    ---------
    x | X | 0

    :return: none. We are operating on global  list board
    '''
    # using .join instead of print(board[0] + ' | '+ board[1] + ' | ' +board[2])
    system('cls')
    print(' | '.join(board[0:3]))
    print('-'*9)
    print(' | '.join(board[3:6]))
    print('-' * 9)
    print(' | '.join(board[6:9]))


def get_input():
    '''
    DOCSTRING :  Takes input between 1-9 and plot respective players input style x/0 in board list.

    :return: none.     We are operating on global  list board
    '''
    position = int(input(f"Player {current_player} Input [1-9])"))
    if current_player == 1 and board[position-1] == '.':   # check == '.' to avoid over writing already entered value.
        board[position-1] = p1_input_style
    if current_player == 2 and board[position-1] == '.':
        board[position-1] = p2_input_style
    print_board(board)



####################################################
#Main program loginc starts here
#####################################################

board= str('. '*9).split()   # create input list with all dots like none played.
win_combination = ['012', '345', '678', '036', '147', '258', '048', '246']

while '.' in board:  # keep asking for inputs until last dot. is not filled.
    if current_player == 2:
        current_player = 1
    else:
        current_player = 2
    # using filter to run a lambda on win combination list. lambda checks if every digit in win combination
    # list item is same as player one input style. If yes then player 1 wins. Lambda will return true to filter
    # if any win combination becomes true and filter will return winning combination in win variable.
    # then we can check if win is not empty list and see if any player has won.
    win = filter(lambda x: board[int(x[0])] == board[int(x[1])] == board[int(x[2])] == p1_input_style,win_combination)
    if list(win):
        print('Player1 Won..!!!!!!')
        exit()
    win = filter(lambda x: board[int(x[0])] == board[int(x[1])] == board[int(x[2])] == p2_input_style, win_combination)
    if list(win):
        print('Player2 Won..!!!!!!')
        exit()

    get_input()


