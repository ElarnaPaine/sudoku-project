# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:41:27 2022
@author: Elarna
"""
import csv

confirmed_start = 0
confirmed_end = 0
for i in range(9):
    for j in range(9):
        if squares[i,j].count(0) == 8:
            confirmed_end += 1
print(confirmed_end)

while confirmed_end < 81:
    if confirmed_end > confirmed_start:
    #removes numbers that are in that row#
        
        
        #removes numbers in that column#
        for i in range(9):
            for j in range(9):
                if squares[i,j].count(0) == 8:
                    number = squares[i,j].index(1)
                    for k in range(9):
                        squares[i,k][number] = 0
                        squares[i,j][number] = 1
        
        #removes numbers repeated in mini grid#
        #REDO IT ALL YOU WHORE#
        grid_ranges = [(0,1,2),(3,4,5),(6,7,8)]
        for i_value in grid_ranges:
            for i in i_value:
                for j_value in grid_ranges:
                    for j in j_value:
                        if squares[i,j].count(0) == 8: 
                            number = squares[i,j].index(1)
                            for i_value in grid_ranges:
                                for a in i_value:
                                    for j_value in grid_ranges:
                                        for b in j_value:
                                            squares[a,b][number] = 0
                                            squares[i,j][number] = 1
    
        #removing squares that can only be that square#
        #AND THIS ONE TOO, SLAG#
        for index_place in range(9):
            counter = 0
            for i in grid_ranges[2]:
                for j in grid_ranges[1]:
                        if squares[i,j].count(1) != 1:
                            if squares[i,j][index_place] == 1:
                                counter += 1
            if counter == 1:
                squares[i,j] = [0,0,0,0,0,0,0,0,0]
                squares[i,j][index_place] = 1
                print(i, j, squares[i,j])
                    
        confirmed_start = confirmed_end
    
        confirmed_end = 0
        for i in range(9):
            for j in range(9):
                if squares[i,j].count(0) == 8:
                    confirmed_end += 1
        print(confirmed_end)
    else:
        print('needs another alogrithm')
        break 
for i in range(9):
    for j in range(9):
        squares[i,j]= squares[i,j].index(1)+1
 
final_solution = []
for j in range(9):
    solution = []
    for i in range(9):
        solution.append(squares[i,j])
    final_solution.append(solution)

with open('example_3_solution.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(final_solution)