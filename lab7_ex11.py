# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 08:53:43 2024

@author: motil
"""
#Enter integer and build a list
def input_list(n):
    a=[]
    list=n+1
    while n!=0:
        num=int(input("%d.Enter integer:"%(list-n)))
        a.append(num)
        n-=1
    return a
#Create new list ,numbers that smaller than X on the left and bigger on the right
def create_new_list(a,x):
    new_list=[]
    for i in range(len(a)):
        if a[i]<x:
            new_list.append(a[i])
    for i in range(len(a)):
        if a[i]>=x:
            new_list.append(a[i])
    return new_list
def main():
    n=7
    a=input_list(n)
    x=int(input("Enter x:"))
    new=create_new_list(a,x)
    print("Original list:" ,a)
    print("New list:",new)
    
main()
    
    
        
            
        
    
            
            
            
            
            
            
            
            
    