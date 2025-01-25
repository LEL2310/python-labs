# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:56:24 2024

@author: motil
"""

def sum_num(num):
    total=0
    while num>0:
        total=total+num%10
        num=num//10
    return total
def main():
    num=int(input("Enter intiger number:"))   
main()
            
            
    