# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:13:12 2025

@author: motil
"""
#Checks if the sum of the row equals it's row number
def equal_row(mat,n):
    sum=0
    for i in range(len(mat[n])):
        sum+=mat[n][i]
    if sum==n:
        return True
    else:
        return False
#checks if all the numbers on the main cross are posotive
def pos_cross(mat):
    for i in range(len(mat)):
        if mat[i][i]<0:
            return False
        return True

  #print the matrix as a table              
def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print("%5d"%mat[i][j],end='')
        print()
    

def main():
    size=5
    matrix=[]
#build the matrix
    for i in range(size):
        row=[]
        for j in range(size):
            row.append(int(input()))
        matrix.append(row)
    print("The matrix is:")
    print_matrix(matrix)
#checks equal ans positive on each row 
    for i in range(size):
        e=equal_row(matrix,i)
        p=pos_cross(matrix)
#print the suitable message
    if e==False and p==False:
        print("The matrix is illegal!")
    if e==False or p==False:
        print("The matrix is illegal!")
    if e==True and p==True:
        print("The matrix is legal!")

main() 



    
        