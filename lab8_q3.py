# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:13:46 2025

@author: motil
"""
#check if there are similiar chars next to each other 
def similar_letter(str):
    new_st=""
    for i in range(len(str)):
#if the chars are the same it drops one of them 
        if str[i:i+1]!=str[i-1:i]:
            new_st+=str[i]
    return new_st
    


def main():
    st=input("Enter a string, please:")
    n=similar_letter(st)
    print("After removing all duplicates:",n)
    
main()
    
    