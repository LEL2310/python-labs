# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:46:49 2024

@author: motil
"""

def main():
    n=int(input("Enter a natural number:"))
    sum=0
    for i in range(1,n+1):
        sum+=i
    print("The triangle number in location %d is:%d"%(n,sum))
main()
    