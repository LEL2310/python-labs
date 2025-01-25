# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 12:03:56 2024

@author: motil
"""

def build_set():
    n=int(input("Enter the size of set A: "))
    print("Enter 4 natural numbers between 1 to 100, with no repetitions ")
    A=[]
    len=0
    while len<n:
        num=int(input())
        if num<1 or num>100:
            print ("wrong input")
            num=int(input())
        if num in A:
            print("Wrong input")
            num=int(input())
        A.append(num)    
        len+=1
    print(A)
    
    
build_set()
