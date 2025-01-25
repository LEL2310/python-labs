# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 08:45:08 2025

@author: motil
"""
#checks if the matrix is perfect(same num cant appear twice at the same row/col num has to be smaller that n)
def is_perfect_mat(mat):
    n=len(mat)
#checks that the matrix has just numbers from 1 to n
    for i in range(n):
        for j in range(n):
            if mat[i][j]<1 or mat[i][j]>n:
                return False
#checks if there is a number that apear more than one at the cols
    for c in range(n):
        check=[0]*(n+1)
        for r in range(n):
            check[mat[r][c]]+=1
        for x in range(1,n+1):
            if check[x]>1:
                return False
#checks if there is a number that apear more than one at the rows
    for r in range(n):
        check=[0]*(n+1)
        for c in range(n):
            check[mat[r][c]]+=1
        for x in range(1,n+1):
            if check[x]>1:
                return False
    return True
#prints the matrix 
def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print("%6i" %mat[i][j],end='')
        print()
def main():
    flag=True
    while flag==True:
        n=int(input("Enter the matrix dimension:"))
#checks that the matrix size is not zero
        if n==0:
            flag=False
            print("Finish")
        else:
             print ("Enter the entries rowwise:")
#asks numbers in len n and build matrix
             matrix=[]
             for i in range(n):
                 row=[]
                 for j in range(n):
                     row.append(int(input()))
                 matrix.append(row)
             print_matrix(matrix)
             if is_perfect_mat(matrix)==True:
                 print("The matrix is perfect")
             else:
                 print("The matrix is not perfect")
                
main()
   
            
            
            