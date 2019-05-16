import math  # standard library

import numpy as np   # 3rd party packages
import pandas as pd


example = np.array([["", "", "", 2, 6, "", 7, "", 1],
                    [6, 8, "", "", 7, "", "", 9, ""],
                    [1, 9, "", "", "", 4, 5, "", ""],
                    [8, 2, "", 1, "", "", "", 4, ""],
                    ["", "", 4, 6, "", 2, 9, "", ""],
                    ["", 5, "", "", "", 3, "", 2, 8],
                    ["", "", 9, 3, "", "", "", 7, 4],
                    ["", 4, "", "", 5, "", "", 3, 6],
                    [7, "", 3, "", 1, 8, "", "", ""]])

def loadSudoku():
    ''' loads sudoku from excel, format as rows '''

    file = 'test.xlsx'                    # Assign spreadsheet filename to `file`
    xl = pd.ExcelFile(file)               # Load spreadsheet
    df = xl.parse('Sheet1')               # Load a sheet into a DataFrame by name: df1
    df = df.drop('Unnamed: 0', axis=1)    # remove first column
    df = df.drop(0, axis=0)               # remove first row
    df = df.fillna("")                    # replace NaN values with blank strings
    df = df.values                        # convert to NumPy array
    df = np.array(df, dtype='U1')         # change data type
    sudoku = df

    return sudoku

class SudokuSolver:
    ''' class to solve a sudoku '''

    def __init__(self, sudoku):
        ''' example sudoku, as rows '''

        self.sudoku = sudoku
        self.sudoSize = len(self.sudoku)
        self.boxSize = int(math.sqrt(self.sudoSize))
        self.complete = np.linspace(1, self.sudoSize, num=self.sudoSize, dtype='b')

    def numChecker(self):
        ''' checks which numbers are in the rows and columns '''

        colNum = 1  # column number
        rowNum = 1  # row number

        for row in self.sudoku:

            for element in row:

                if self.sudoSize >= 9: # change
                    box1 = self.sudoku[0:self.boxSize,0:self.boxSize].flatten()
                    box2 = self.sudoku[0:self.boxSize,self.boxSize:self.boxSize*2].flatten()
                    box3 = self.sudoku[0:self.boxSize,self.boxSize*2:self.boxSize*3].flatten()
                    box4 = self.sudoku[self.boxSize:self.boxSize*2,0:self.boxSize].flatten()
                    box5 = self.sudoku[self.boxSize:self.boxSize*2,self.boxSize:self.boxSize*2].flatten()
                    box6 = self.sudoku[self.boxSize:self.boxSize*2,self.boxSize*2:self.boxSize*3].flatten()
                    box7 = self.sudoku[self.boxSize*2:self.boxSize*3,0:self.boxSize].flatten()
                    box8 = self.sudoku[self.boxSize*2:self.boxSize*3,self.boxSize:self.boxSize*2].flatten()
                    box9 = self.sudoku[self.boxSize*2:self.boxSize*3,self.boxSize*2:self.boxSize*3].flatten()

                col = self.sudoku[:,colNum - 1]

                # get values associated with cell
                if colNum <= self.boxSize and rowNum <= self.boxSize:
                    nonValues = np.concatenate((row, col, box1), axis=0)

                elif self.boxSize < colNum <= self.boxSize*2 and rowNum <= self.boxSize:
                    nonValues = np.concatenate((row, col, box2), axis=0)

                elif colNum > self.boxSize*2 and rowNum <= self.boxSize:
                    nonValues = np.concatenate((row, col, box3), axis=0)

                elif colNum <= self.boxSize and self.boxSize < rowNum <= self.boxSize*2:
                    nonValues = np.concatenate((row, col, box4), axis=0)

                elif self.boxSize < colNum <= self.boxSize*2 and self.boxSize < rowNum <= self.boxSize*2:
                    nonValues = np.concatenate((row, col, box5), axis=0)

                elif colNum > self.boxSize*2 and self.boxSize < rowNum <= self.boxSize*2:
                    nonValues = np.concatenate((row, col, box6), axis=0)

                elif colNum <= self.boxSize and rowNum > self.boxSize*2:
                    nonValues = np.concatenate((row, col, box7), axis=0)

                elif self.boxSize < colNum <= self.boxSize*2 and rowNum > self.boxSize*2:
                    nonValues = np.concatenate((row, col, box8), axis=0)

                else:
                    nonValues = np.concatenate((row, col, box9), axis=0)

                nonValues = np.unique(nonValues)        # remove duplicates
                nonValues = nonValues[nonValues!=""]    # remove blanks

                if nonValues.size == self.sudoSize - 1 and element == "":    # one remaining value and an empty box
                    nonValues = np.array(nonValues, dtype='b')    # convert to signed byte for data consistency
                    missing_value = int(np.setdiff1d(self.complete, nonValues))
                    self.sudoku[rowNum - 1, colNum - 1] = missing_value

                colNum += 1

                if colNum == self.sudoSize + 1:   # reset column counter
                    colNum = 1

            rowNum += 1

            if rowNum == self.sudoSize + 1:   # reset row counter
                rowNum = 1
