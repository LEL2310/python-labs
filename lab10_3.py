# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:56:09 2025

@author: motil
"""
#does binary search to find the smallest number
def  minShiftedList(s_lst,n):
    low,high=0,n-1
    while low<high:
        mid=(low+high)//2
        if s_lst[mid]<s_lst[high]:
            high=mid
        else:
            low=mid+1
    return s_lst[low]
def main():
    print("Please enter ordered and shifted sequence of numbers (end with -1):")
    s_lst=[]
    flag=True
#asks from the user to enter integers in sorted and shifted way 
    while flag==True:
        num=int(input())
#to stop the loop enter -1
        if num ==-1:
            flag=False
        else:
            s_lst.append(num)
    n=len(s_lst)
    m=minShiftedList(s_lst, n)
    print("The smallest number is:",m)
main()