# -*- coding: utf-8 -*-

# simple sudoku solver! ver 1.0 by GIG

import numpy as np
import pandas as pd

complete = np.linspace(1,9,num=9,dtype='b')


def load_sudoku():
    ''' loads sudoku from excel, format as rows '''
    
    file = 'test.xlsx'          # Assign spreadsheet filename to `file`
    xl = pd.ExcelFile(file)     # Load spreadsheet
    df1 = xl.parse('Sheet1')    # Load a sheet into a DataFrame by name: df1
    df1 = df1.drop(0, axis=1)   # remove first column
    df1 = df1.fillna("")        # replace NaN values with blank strings
    df1 = df1.values            # convert to NumPy array
    df1 = np.array(df1, dtype='U1') # change data type
    sudoku = df1
    
    return sudoku

sudoku = load_sudoku()

def num_checker():
    ''' replaces missing values '''
    
    col_num = 1  # column number
    row_num = 1  # row number

    for row in sudoku:
        for element in row:

            box1 = sudoku[0:3,0:3].flatten()
            box2 = sudoku[0:3,3:6].flatten()
            box3 = sudoku[0:3,6:9].flatten()
            box4 = sudoku[3:6,0:3].flatten()
            box5 = sudoku[3:6,3:6].flatten()
            box6 = sudoku[3:6,6:9].flatten()
            box7 = sudoku[6:9,0:3].flatten()
            box8 = sudoku[6:9,3:6].flatten()
            box9 = sudoku[6:9,6:9].flatten()
            
            col = sudoku[:,col_num-1]
            
            # combines the values of rows, columns and boxes for each element
            if col_num < 4 and row_num < 4:
                non_values = np.concatenate((row, col, box1), axis=0)
           
            elif 3 < col_num < 7 and row_num < 4:
                non_values = np.concatenate((row, col, box2), axis=0)
            
            elif col_num >= 7 and row_num < 4:
                non_values = np.concatenate((row, col, box3), axis=0)
            
            elif col_num < 4 and 3 < row_num < 7:
                non_values = np.concatenate((row, col, box4), axis=0)
           
            elif 3 < col_num < 7 and 3 < row_num < 7:
                non_values = np.concatenate((row, col, box5), axis=0)
            
            elif col_num >= 7 and 3 < row_num < 7:
                non_values = np.concatenate((row, col, box6), axis=0)

            elif col_num < 4 and row_num >= 7:   
                non_values = np.concatenate((row, col, box7), axis=0)
           
            elif 3 < col_num < 7 and row_num >= 7:
                non_values = np.concatenate((row, col, box8), axis=0)
            
            else:
                non_values = np.concatenate((row, col, box9), axis=0)
            
            non_values = np.unique(non_values)         # remove duplicates
            non_values = non_values[non_values!=""]    # remove blanks
            
            if non_values.size == 8 and element == "":    # one remaining value and an empty box
                non_values = np.array(non_values, dtype='b')    # convert to signed byte for data consistency
                missing_value = int(np.setdiff1d(complete, non_values))
                sudoku[row_num-1, col_num-1] = missing_value
                
            col_num += 1

            if col_num == 10:   # reset column counter
                col_num = 1

        row_num += 1

        if row_num == 10:   # reset row counter
            row_num = 1


if __name__ == "__main__":
  load_sudoku() # loads soduku from excel file
  for i in range(50):
      num_checker()
      if "" not in sudoku:
          print(sudoku)
          print("complete!")
          break