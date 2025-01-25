# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:11:21 2025

@author: motil
"""
#turns a string to a number only if the chars represent numbers
def check_num(str):
    if str=="":
        return 0
    digit=ord(str[0])-ord('0')
    if digit>0 and digit<9:
#creates the number 
        return digit * (10 ** (len(str) - 1)) + check_num(str[1:])
    
def main():
    st=input("Please enter a string:")
#checks every char in the string if represent a number 
    for x in st:
        if not(x>='0' and x<='9'):
            print("The string is illegal!")
            return
    num=check_num(st)
    print("The string %s corresponds to the number %d."%(st,num))
     
main()            
    