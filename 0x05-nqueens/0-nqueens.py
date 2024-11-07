#!/usr/bin/python3
"""An answer to the N-Queens puzzle"""
import sys

def print_board(board, n):
    """Prints allocated positions for the queens"""
    print([[i, board[i]] for i in range(n)])

def safe_position(board, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def determine_positions(board, row, n):
    """Recursively finds all safe positions to place the queens"""
    if row == n:
        print_board(board, n)
    else:
        for col in range(n):
            if safe_position(board, row, col):
                board[row] = col
                determine_positions(board, row + 1, n)
                board[row] = -1  # Backtrack

def create_board(size):
    """Generates the board"""
    return [-1] * size  # Use -1 to represent empty rows

# Argument validation
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Run the N-Queens solution
board = create_board(n)
determine_positions(board, 0, n)

