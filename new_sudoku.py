# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:44:26 2022
@author: Elarna
"""

import csv
def sudoku_set_up(sudoku_name):
    cell = [[] for i in range(9)]
    for i in range(9):
        cell[i]= [[1,1,1,1,1,1,1,1,1] for i in range(9)]
    
    fname = sudoku_name + '.csv'
    with open(fname) as csvfile:
        squares_reader = csv.reader(csvfile)
        j = 0 
        for row in squares_reader:
            for i in range(9):
                if row[i] != '':
                    cell[i][j] = [0,0,0,0,0,0,0,0,0]
                    cell[i][j][int(row[i])-1] = 1               
            j += 1
    return cell

def sudoku_eliminate_row(cell):
    for i in range(9):
            for j in range(9):
                if cell[i][j].count(0) == 8:
                    number = cell[i][j].index(1)
                    for k in range(9):
                        cell[k][j][number] = 0
                        cell[i][j][number] = 1
    return cell 

def sudoku_eliminate_column(cell):
    for i in range(9):
            for j in range(9):
                if cell[i][j].count(0) == 8:
                    number = cell[i][j].index(1)
                    for k in range(9):
                        cell[i][k][number] = 0
                        cell[i][j][number] = 1
    return cell 

def sudoku_eliminate_grid(cell):
    sudoku_range = [[0,1,2],[3,4,5],[6,7,8]]
    for i in range(len(sudoku_range)):
        list_i = sudoku_range[i]
        for j in range(len(sudoku_range)):
            list_j = sudoku_range[j]
            for i_2 in list_i:
                for j_2 in list_j:
                    
                    if cell[i_2][j_2].count(0) == 8:
                        i_number = i_2
                        j_number = j_2
                        number = cell[i_2][j_2].index(1)
                        
                        for x in list_i:
                            for y in list_j:
                                cell[x][y][number] = 0
                        cell[i_number][j_number][number] = 1
                
    return cell
                       
def sudoku_strategy(sudoku_name):
    x = sudoku_set_up(sudoku_name)
    x = sudoku_eliminate_grid(sudoku_eliminate_column(sudoku_eliminate_row(x)))
    
    filled_cells = 0
    last_count = 0
    
    while last_count < 81:
        if last_count >= filled_cells:
            x = sudoku_eliminate_grid(sudoku_eliminate_column(sudoku_eliminate_row(x)))
            for i in range(9):
                for j in range(9):
                    if x[i][j].count(0) == 8:
                        filled_cells += 1
            x = sudoku_eliminate_grid(sudoku_eliminate_column(sudoku_eliminate_row(x)))
            last_count = filled_cells
            filled_cells = 0
        else:
            print('Another strategy needed')
            break 
    
    for i in range(9):
        for j in range(9):
            x[i][j]= x[i][j].index(1)+1
    final_solution = []
    for j in range(9):
        solution = []
        for i in range(9):
            solution.append(x[i][j])
        final_solution.append(solution)
    with open(sudoku_name + '_solution.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(final_solution)
    return x
    
def main():
    return sudoku_strategy('example_new')