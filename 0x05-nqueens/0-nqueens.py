#!/usr/bin/python3
"""Solution to the N-Queens puzzle"""
import sys


def print_board(board, n):
    """Prints allocated positions of the queens."""
    solution = [[i, board[i]] for i in range(n)]
    print(solution)


def safe_position(board, row, col):
    """Checks if the position is safe for a queen."""
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def determine_positions(board, row, n):
    """Recursively finds all safe positions for queens."""
    if row == n:
        print_board(board, n)
    else:
        for col in range(n):
            if safe_position(board, row, col):
                board[row] = col
                determine_positions(board, row + 1, n)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

board = [-1] * n
determine_positions(board, 0, n)

