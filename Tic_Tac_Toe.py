##### Mini-max 


import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is full
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    # Get empty cells on the board
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'O'):
        return -1
    elif is_winner(board, 'X'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Cell already taken. Try again.")
            continue

        # Check for player win
        if is_winner(board, 'O'):
            print_board(board)
            print("Congratulations! You win!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = 'X'

        # Check for AI win
        if is_winner(board, 'X'):
            print_board(board)
            print("AI wins! Better luck next time.")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()

