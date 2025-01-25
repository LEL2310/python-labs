# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:44:34 2024

@author: motil
"""

def main():
    num=int(input("Please enter a 4-digits natural number:"))
    if num<0:
        print("%d isn't a natural number."%num)
    elif not(1000<=num<=9999):
        print("%d isn't a 4-digits number"%num)
    else:
        d1=num%10
        d2=(num//10)%10
        d3=(num//100)%10
        d4=num//1000
        diff1=d2-d1
        diff2=d3-d2
        diff3=d4-d3
        if d1==d2==d3==d4:
            print("All digits are the same.")
        elif d1>=d2>=d3>=d4:
            if diff1==diff2==diff3:
                print("Increasing arithmetic sequence.")
            else:
                print("Increasing sequence.")
        elif d1<=d2<=d3<=d3:
            if diff1==diff2==diff3:
                print("Decreasing arithmetic sequence.")
            else:
                print("Decreasing sequence.")
        else:
            print ("Not increasing and not decreasing.")
main()

        
        