# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:07:54 2024

@author: motil
"""

def main():
    num=int(input("Enter 3-digits number:"))
    if num>=100 and num<=999:
        right=num%10
        mid=(num//10)%10
        left=num//100
        if left%2==0:
            left+=1
        else:
            left-=1
        if mid%2==0:
            mid+=1
        else:
            mid-=1
        if right%2==0:
            right+=1
        else:
            right-=1
        new_num=left*100+mid*10+right
        print("The result is:",new_num)
    else:
        print("wrong input")
main()
    
        
        