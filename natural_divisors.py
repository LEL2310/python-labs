# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:11:57 2024

@author: motil
"""

def main():
    count=0 
    num=(int(input("Enter a natural number:")))
    #check if the number is natural
    if num<=0:
        print("Input is not a natural number")
    else:
        print("The list of natural divisors of %d is:"%(num),end='')
        #check the number of natural divisors for num and count them
        for i in range(1,num+1):
            if num%i==0:
                count+=1
                print("%d"%i,end=',')
            print("\nThe amount of divisors is:%d"%count)
main()