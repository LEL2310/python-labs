# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:25:58 2024

@author: motil
"""
#Build a list of apearance at the number 
def my_digits(num):
    check=[0]*10
    num=abs(num)
    while num>0 :    
        digit=num%10
        check[digit]+=1
        num//=10
    is_all_zero = True
    for c in check:
        if c != 0:
            is_all_zero = False
    if is_all_zero:
        check[0]=1
    return check
#Checkes how many times apears each number
def max_count(check):
    max_count=0
    for i in range(len(check)):
        if check[i]>max_count:
            max_count=check[i]
    return max_count
#checks which is the digit that apears the most and how many times it apears 
def max_digit(check):
    max_digits=[]
    for i in range(len(check)):
        if check[i]==max_count(check):
            max_digits.append(i)
    return max_digits
#prints the data 
def print_data(num):
    checker=my_digits(num)
    for i in range(10):
        if checker[i]>0:
            print("The digit %d appears %d times"%(i,checker[i]))
    m= max_count(checker)
    md=max_digit(checker)
    print("The most frequent digit/s is/are :",end="")
    for digit in md:
        print(digit, end=" ")
    print()
    print("It occurs times",m)
    print()
 #prints the data as long as the num isnt 0, if the num is 0 it prints the data but stop asking for more nums       
def main():
    flag=True
    while flag:
        num=int(input("Enter integer:"))
        if num!=0:
            print_data(num)
        else:
            print_data(num)
            flag=False
        
    
        

main()
        
        
        
            