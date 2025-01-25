# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:31:06 2024

@author: motil
"""

def circ_shift(L):
    first=L[0]
    for i in range(1, len(L)):
       L[i-1]=L[i]
    L[len(L)-1]=first
def main():
    a=[]
    print("Enter 5 numbers:")
    for i in range(5):
        a.append(int(input()))
    print('before shift: a=',a)    
    circ_shift(a)
    print('after shift: a=',a)
main()