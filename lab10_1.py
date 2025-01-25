# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 08:41:09 2025

@author: motil
"""

#create new list that turn big letters to little letters
def lit_letters(str):
    l_letters=""
    for i in range(len(str)):
        if str[i]>='a' and str[i]<='z':
            l_letters+= str[i]
        elif  str[i]>='A' and  str[i]<='Z':
            lit=ord( str[i])+(ord('a')-ord('A'))
            l_letters+=chr(lit)
    return l_letters
#check which letter is thr most frequent one
def most_frequent_letter(ls):
    apear=[0]*26
    max=0
    max_i=-1
    lst=lit_letters(ls)
    for ch in lst:
        if ch>='a' and ch<='z':
            apear[ord(ch)-ord('a')]+=1
    for i in range(26):
        if max<apear[i]:
            max=apear[i]
            max_i=i
#check if there are letters in the string 
    if max==0:
        return -1 
    return chr(ord('a')+max_i)
    
    
def main():
    flag=True
#ask for string while the string is not quit 
    while flag==True:
        str=input("Enter a string, please:")
        if str=='quit' or str=='Quit':
            print("Thank you for exploring strings and complexity")
            flag=False
        if flag==True:
            most=most_frequent_letter(str)
            if most==-1:
                    print ("-1")
            else:
                print("The most frequent letter is:",(most))

main()
        
        
    
    
    
    
    
        
        
        
        
    
            
        