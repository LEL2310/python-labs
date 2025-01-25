# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:46:21 2025

@author: motil
"""
#Lihi Elias:319041109
#Yasmin Askarov:323017012

#checks if sub matrix is in original matrix retrun true or false
def an_occurence(m1,m2,l,a):
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            if i + l >= len(m1) or j + a >= len(m1[0]) or m1[i + l][j + a] != m2[i][j]:
                return False
    return True
#prints the sub matrix
def print_sub(mat,R,C):
    for i in range(R):
        for j in range(C):
            print(("%5s"%mat[i][j]),end='')
        print()
#checks if the original matrix if periodic return true or false
def is_periodic (mat,R,C):
    rows=len(mat)
    cols=len(mat[0])
#checks if originals rows and cols divisible with sub rows and cols
    if rows%R!=0 or cols%C!=0:
        return False
#build sub matrix 
    s_mat=[]
    for i in range(R):
        r_mat=[]
        for j in range(C):
            r_mat.append(mat[i][j])
        s_mat.append(r_mat)
    flag=False
    for r in range(0,rows,R):
        for c in range(0,cols,C):
            if flag==an_occurence(mat, s_mat, r, c):
                return False
    return True

def main():
    rows,cols=eval(input("Enter matrix dimensions:"))
    print("Enter %d elements:"%(rows*cols))
#build the original matrix
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append((input()))
        matrix.append(row)
    flag=False
#checks if the original matrix is periodic if true prints the sub matrix 
    for R in range(1,rows-1):
        for C in range(1,cols-1):
            if not flag and is_periodic(matrix, R, C)==True:
                print("The matrix is periodic")
                print("The sub-matrix is:")
                print_sub(matrix,R,C)
                flag=True
    if not flag:
        print("The matrix is not periodic.")

main()