# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 09:33:01 2025

@author: motil
"""
#If there are big letters it returns it to little letters 
def lit_letters(str):
    l_letters=""
    for i in range(len(str)):
#check if the letter is already small and if not it turns it from big to small
        if str[i]>='a' and str[i]<='z':
            l_letters+= str[i]
        elif  str[i]>='A' and  str[i]<='Z':
            lit=ord( str[i])+(ord('a')-ord('A'))
            l_letters+=chr(lit)
            
    return l_letters
#check which letter is the biggest one in the string 
def max_letter(str):
    str1=lit_letters(str)
    max='a'
#check if there are letters at all
    if not str1:
        return "There were no letters"
    for ch in str1:
        if ch>='a' and ch<='z':
            if ch>max:
                max=ch
        
    return max
#check which letter is the smallest in the string 
def min_letter(str):
    str1=lit_letters(str)
    min='z'
    if not str1:
        return "There were no letters"
    for ch in str1:
        if ch>='a' and ch<='z':
            if ch<=min:
                min=ch

    return min
    

def main():
    st=str(input("Enter your sentence:"))
    max_le=max_letter(st)
    min_le=min_letter(st)
    if min_le=="There were no letters" and max_le=="There were no letters":
        print("There were no letters")
    else:
        print("Largest and smallest letters are:",max_le, min_le)
        
main()           
            
            
        
    