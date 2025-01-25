# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:37:59 2025

@author: motil
"""
#Takes the second string and add it to the first string for place x
def combineStr(s1,s2,x):
    new_s=""
    new_s3=""
    for i in range(len(s1)):
        if x==i:
#Turns little letters to big letters
            for ch in s2:
                big=ord(ch)-(ord('a')-ord('A'))
                new_s+=chr(big)
            new_s3=s1[:x]+new_s+s1[x:]
    return new_s3

def main():
    s1=str(input("Enter the first string:"))
    s2=str(input("Enter the second string:"))
    x=int(input("Enter index x:"))
    com=combineStr(s1, s2, x)
#Checks that the value of x is valid
    if x<0:
        print("Invalid index")
    else:
        print("combined string",com)
main()
        
                
            

        
                  
    