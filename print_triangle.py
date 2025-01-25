# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:35:09 2024

@author: motil
"""
def print_triangle(ch,num):
    for i in range(num):
        for j in range(num-i):
            print(ch,end=' ')
        print()
def main():
    ch=input("Enter a letter:")
    num=int(input("Enter an integer:"))
    print("***Triangle***")
    print_triangle(ch,num)
main()
