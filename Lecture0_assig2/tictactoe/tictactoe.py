"""
Tic Tac Toe Player
"""

import copy
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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions            
    # raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board [action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")
    modified_board = copy.deepcopy(board)
    # modified_board = deepcopy(board)
    turn = player(board)
    modified_board[action[0]][action[1]] = turn
    return modified_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows and columns
    for i in range(len(board)):
            if  board[i][0] == board[i][1] == board[i][2] != EMPTY:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != EMPTY:
                return board[0][i]
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None
        
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win is not None:
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board [i][j] == EMPTY:
                return False
    return True
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0    
    # raise NotImplementedError


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     if terminal(board) == True:
#         return None
#     turn = player(board)
#     possible_moves = actions(board)
#     # O_win = set()
    
#     for i in range(len(possible_moves)):
#         possible_board = result(board, possible_moves(i))
#         win_ = utility(possible_board)
#         if turn == 'X':
#             if win_ == -1:
#                 return possible_moves[i]
#         if turn == 'O':
#             if win_ == 1:
#                 return possible_moves[i]            
#             # O_win.add(possible_moves)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current = player(board)

    if current == 'X':
        best_value = float('-inf')
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_move

    else:  # current == 'O'
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


    # raise NotImplementedError
