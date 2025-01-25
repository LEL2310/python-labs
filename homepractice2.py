# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:35:20 2024

@author: motil
"""

def main():
    num1,num2=eval(input("Insert two numbers:"))
    flag=False
    place=0
    temp=num1
    carry=0
    result=0
    while temp!=0:
        if temp%10>=7:
            flag=True
            temp//=10
    temp=num2
    while temp!=0:
        if temp%10>=7:
            flag=True
            temp//=10
    if flag:
        print("Illegal input")
    else:
        sum=0
        end=0
        while end!=-1:
            if num1==0 and num2==0:
                end==-1
            if (num1%10+num2%10+carry)>6:
                sum=(num1%10+num2%10+carry)
                result+=(sum%7)*(10**place)
                carry=1
            elif(num1%10+num2%10+carry)<=6:
                sum=(num1%10+num2%10+carry)
                result+=(sum%7)*(10**place)
                carry=0
            place+=1
            num1//10
            num2//10
        if carry==1:
            result=result+(10**place)
            print("The sum is the 7-base number:",result)
        else:
            print("The sum is the 7-base number:",result)
main()
                
                



            
                
                
                
        