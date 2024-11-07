#!/usr/bin/python3
"""
N queens problem solution using backtracking
"""

import sys

def n_queens(n):
    res, queens = [], []
    cols, pos_diag, neg_diag = set(), set(), set()

    def backtrack(row):
        if row == n:
            res.append(queens[:])
            return
        for col in range(n):
            if col in cols or row + col in pos_diag or row - col in neg_diag:
                continue
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            queens.append([row, col])
            backtrack(row + 1)
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            queens.pop()

    backtrack(0)
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = sys.argv[1]
    if not n.isdigit() or int(n) < 4:
        print("N must be a number" if not n.isdigit() else "N must be at least 4")
        exit(1)
    solutions = n_queens(int(n))
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

