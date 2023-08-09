#!/usr/bin/python
## the module we'll call to check if a sudoku is solveable before presenting to the user

##IMPORTS
import numpy as np
import math
import random

def solve_sudoku(grid, size, row=0, col=0):
    if row == (size - 1) and col == size:
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve_sudoku(grid, size, row, col + 1)
    for num in range(1, size + 1):
        if is_valid(grid, row, col, num, size):
            grid[row][col] = num
            if solve_sudoku(grid, size, row, col + 1):
                return True
        grid[row][col] = 0
    return False