# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:27:23 2025

@author: motil
"""
#check if the list is a palindrom
def is_palindrom(lst):
    if len(lst)<=1:
        return True 
    return lst[0]==lst[-1] and is_palindrom(lst[1:-1])

def main():
    print("Enter a sequence of natural numbers, end with 0:")
    flag=True
    while flag==True:
        num=int(input())
#the condition that stops the loop 
        if num==0:
            print("Finish")
            flag=False
        else:
            list=[]
#build a list from the number 
            while num!=0:
                list.append(num%10)
                num//=10
            if is_palindrom(list):
                print("The list of digits is a palindrom")
            if not is_palindrom(list):
                print("The list of digits is not a palindrom")

main()
        
    
        