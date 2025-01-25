# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:28:19 2025

@author: motil
"""
#check if the matrix is extreme
def is_extreme(mat):
    n=len(mat)
    if n!=len(mat[0]):
        return False
#checks the rows in places that defined in main cross and sec cross 
    for i in range(n):
        main_cross=mat[i][i]
        sec_cross=mat[i][n-1-i]
#if the num in sec cross is bigger that in main cross it's not an extreme mat
        if main_cross<sec_cross:
            return False
    return True

def main():
    print('first matrix:')
    m_1=[[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5]]
    print(m_1)
    print('is extreme matrix:',is_extreme(m_1))
    
    print('second matrix:')
    m_2=[[5,2,3,4,2],[6,7,8,3,0],[1,2,4,4,5],[1,2,3,4,5]]
    print(m_2)
    print('is extreme matrix:', is_extreme(m_2))
    
    
    print('third matrix:')
    m_3=[[5,2,3,4,2],[6,7,8,3,0],[1,2,4,4,5],[6,0,8,9,0],[1,2,3,4,5]]
    print(m_3)
    print('is extreme matrix:', is_extreme(m_3))
    
    
    print('fourth matrix:')
    m_4=[[1]]
    print(m_4)
    print('is extreme matrix:', is_extreme(m_4))
    
      
main()