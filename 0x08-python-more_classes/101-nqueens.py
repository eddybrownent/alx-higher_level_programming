#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    # Check if it is safe to place a queen at board[row][col]

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    # Recursive function to solve the N-Queens problem

    # Base case: If all queens are placed, print the solution
    if col >= N:
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 'Q'  # Place the queen at board[i][col]
            solve_nqueens(board, col + 1)  # Recur for the next column
            board[i][col] = '.'  # Backtrack and remove the queen


def print_solution(board):
    # Utility function to print the board configuration
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()


# Check if the number of arguments is correct
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Initialize an empty chessboard
board = [['.' for _ in range(N)] for _ in range(N)]

# Solve the N-Queens problem
solve_nqueens(board, 0)
