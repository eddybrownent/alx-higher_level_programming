#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at the given position
    for i in range(row):
        if board[i] == col or \
                board[i] - col == i - row or \
                board[i] - col == row - i:
                    return False
    return True


def solve_nqueens(board, row, N, solutions):
    # Base case: All queens have been placed
    if row == N:
        solutions.append([(i, board[i]) for i in range(N)])
        return

    # Recursive case: Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)


def print_solutions(N):
    # Check if N is smaller than 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    # Check if the program was called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage:nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    print_solutions(N)
