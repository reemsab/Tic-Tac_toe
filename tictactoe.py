"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for r in board:
        for c in r:
            if c is None:
                o = o + 1 
    x = o % 2                                    
    if(x == 1):
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                a.append((i,j))

    return a



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board)
    b = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
    for i in range(3):
        for j in range(3):
            b[i][j] = board[i][j]
    if b[action[0]][action[1]] == EMPTY:
        b[action[0]][action[1]] = p
    return b

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2] != EMPTY:
            return board[i][2]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] != EMPTY:
            return board[2][i]
    if  board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != EMPTY:
        return board[2][2]
    if  board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != EMPTY:
        return board[2][0]
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return(winner(board) != None or len(actions(board)) == 0)
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == X):     return 1
    if(winner(board) == O):     return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)): return None
    if(player(board) == X):
        return maxplayer(board, actions(board))[1]
    return minplayer(board, actions(board))[1]
    raise NotImplementedError


def minplayer(board, action):
    mn = 2
    c = (0,0)
    m = [2, (0,0)]
    for a in action:
        if terminal(result(board, a)):
            u = utility(result(board, a))
        else: u = maxplayer(result(board, a), actions(result(board, a)))[0] 
        if(u == -1):
            m[0] = u
            m[1] = a
            return m
        if(mn > u):
            mn = u
            c = a

    m[0] = mn
    m[1] = c
    return m

def maxplayer(board, action):
    mx = -2
    c = (0,0)
    m = [-2, (0,0)]
    for a in action:
        if terminal(result(board, a)):
            u = utility(result(board, a))
        else: u = minplayer(result(board, a), actions(result(board, a)))[0]
        if(u == 1):
            m[0] = u
            m[1] = a
            return m
        if(mx < u):
            mx = u
            c = a
    m[0] = mx
    m[1] = c
    return m