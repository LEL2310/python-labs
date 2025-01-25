# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:33:23 2024

@author: motil
"""

def line(cnt,tav):
    for i in range(cnt):
        print(tav,end='')
    print()
def main():
    num=int(input("Enter number:"))
    letter=input("Enter letter:")
    line(num,letter)
main()