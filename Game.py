import tkinter as tk
from tkinter import messagebox
import math

# Constants
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Function to evaluate the board and return a score
def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == AI:
                return 10
            elif row[0] == HUMAN:
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == AI:
                return 10
            elif board[0][col] == HUMAN:
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == AI:
            return 10
        elif board[0][0] == HUMAN:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == AI:
            return 10
        elif board[0][2] == HUMAN:
            return -10

    return 0

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

# Function to find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Function to check if there are moves left on the board
def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

# Function to handle user move
def on_button_click(row, col):
    global board
    if board[row][col] == EMPTY:
        board[row][col] = HUMAN
        buttons[row][col].config(text=HUMAN)
        if check_winner():
            messagebox.showinfo("Game Over", "You win!")
            reset_game()
            return
        elif not is_moves_left(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
            return
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI
        buttons[ai_move[0]][ai_move[1]].config(text=AI)
        if check_winner():
            messagebox.showinfo("Game Over", "AI wins!")
            reset_game()
            return
        elif not is_moves_left(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()

# Function to check for a winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return True

    return False

# Function to reset the game
def reset_game():
    global board
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=EMPTY)

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create the board and buttons
board = [[EMPTY for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=EMPTY, width=10, height=3,
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

root.mainloop()
