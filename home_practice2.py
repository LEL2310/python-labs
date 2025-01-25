# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:19:28 2024

@author: yasmi
"""
#Lihi Elias:319041109
#Yasmin Askarov:323017012
def main():
    num1,num2=eval(input("Insert two numbers in base 7:"))
    flag=False
    counter=0
    carry=0
    temp=num1
    #Check that the first number is in base 7 
    while temp !=0:
        if temp%10>=7:
            flag=True
        temp//=10
    #Check that the second number is in base 7    
    temp=num2
    while temp !=0:
        if temp%10>=7:
            flag=True
        temp//=10
    #When the flag is changing the number is illegal    
    if flag:
        print("Illegal input")
        
    else:
        sum=0
        end = 0
    #Check the terms as long as end isn't 1, it will change to 1 when there are no numbers left
        while end != 1:
            if num1 == 0 and num2 == 0:
                end = 1
    #When the number is bigger then 6 there is a carry that the program needs to consider
            if (num1%10 + num2%10 + carry) > 6:
                sum+=((num1%10 + num2%10 + carry)%7)*10**counter
                carry = 1
    #When the number [0,6] there is no carry that the program needs to consider
            elif (num1%10 + num2%10 + carry) <= 6:
                sum+=(num1%10+num2%10+carry)*10**counter
                carry=0
            counter+=1
            num1//=10
            num2//=10
    #When there is a carry that left after num1 and num2 equal 0 the program will move it one place forward
        if carry == 1:
            sum+= 10**counter
            print("The sum is the 7-base number", sum)
        else:
            print("The sum is the 7-base number", sum)
main()