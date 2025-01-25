# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:07:18 2024

@author: motil
"""
#ליהי אליאס:319041109
#יסמין אסקרוב:323017012
#Ask from the user numbers and build a list
def build_list():
    series=int(input("Enter integer numbers > 0, end with -1:\n"))
    a=[series]
    while series != -1:
        series=int(input())
        a.append(series)
    return a 
#Gets a list and turning it into numbers deviding by comma
def print_list(a):
    for i in range(len(a)-1):
        if i!=len(a)-2:
            print(a[i],end=",")
        else:
            print(a[i],end="")
    print()
#Takes a number and shifted it for one time   
def clockwise_shift(n):
    if n<10:
        return n
    new_n=0
    sep=0
    place=1
    while n//10!=0 :
        sep=n%10
        new_n=new_n+sep*10**place
        place +=1
        n=n//10
    new_n=n+new_n
    return new_n
#Uses the function clockwise shift that can only shift one time and shifted the number for n times
def clockwise_shift_n(n,m):
    for i in range(m):
        n=clockwise_shift(n)
    return n
#Uses the function clocwise shift n and defind it how many times to shift each number and bulid a list of the new numbers
def shift_all(numbers):
    shifted_nums=[]
    for i in range(len(numbers)):
        shifted_nums.append(clockwise_shift_n(numbers[i], i))
    return shifted_nums
#Print the original list and then print the list after shifted
def main():
    f_list=build_list()
    print("The initial list is:",end=" ")
    print_list(f_list)
    a_num=shift_all(f_list)
    print("The list after it's items clockwise shifting is:",end=" ")
    print_list(a_num)
main()
    
    