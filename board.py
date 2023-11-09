import numpy as np


# Initialize the chess board using NumPy
board = np.zeros((8, 8), dtype=object)  # Using 'object' to allow different representation of pieces


# A function to represent the board to console
def print_chess_board(board):
    print("  a b c d e f g h")
    print(" +-----------------")
    rank = 8
    for row in board:
        print(f"{rank}| {' '.join(str(cell) for cell in row)}")
        rank -= 1
    print(" +-----------------")
