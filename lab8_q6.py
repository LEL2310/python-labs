# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:02:06 2025

@author: motil
"""
#Finds the index of the row that has the most positive numbers
def most_pos(mat):
    max_positive=0
    max_row=0
#Every time the loop mooving to the next row the count is turning zero 
    for i in range(len(mat)):
        count=0
        for j in range(len(mat[i])):
            if mat[i][j]>=0:
                count+=1
#checks the row with the most positive numbers
        if max_positive<count:
            max_positive=count
            max_row=i
                              
    return max_row

def main():
    row=int(input("Enter number of rows:"))
    col=int(input("Enter number of columns:"))
    print("Enter the matrix elements:")
#build list from numbers in the size the user puts (build matrix)
    matrix=[]
    for i in range(row):
        rows=[]
        for j in range(col):
            rows.append(int(input()))
        matrix.append(rows)
    print("The entered matrix is:")
#prints the matrix
    for x in matrix:
        print(x)
    max_index=most_pos(matrix)
    print("The row with the most positive values is:", max_index)
    
main()
    
    
        
    