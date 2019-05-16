#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" sudokuSca.py: Solves a sudoku of any nxn size, with sub-box size of sqrt(n)xsqrt(n). """

__author__ = "Geoff Grevers"
__credits__ = ["Geoff Grevers"]
__version__ = "1.0"
__maintainer__ = "Geoff Grevers"
__email__ = "ggrevers@hotmail.co.uk"
__status__ = "Prototype"

import sudokuSca # local source
from sudokuSca import example, loadSudoku

if __name__ == "__main__":
    # user decides to use example or input their own sudoku
    choice: str = input("Type 'example' (without quotes) to show functionality,\n or to input your own sudoku, type 'my own':")
    if choice == "example":
        s = sudokuSca.SudokuSolver(example) # load instance example soduku
        print("Example:\n", example)
    elif choice == "my own":
        s = sudokuSca.SudokuSolver(loadSudoku())
        print("Your sudoku:\n", loadSudoku())
    else:
        print("invalid input, try again")

    for i in range(50): # tries up to 50 times
        s.numChecker()

        if "" not in s.sudoku:
            print("Solution:\n", s.sudoku)
            break
