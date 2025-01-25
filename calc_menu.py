# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:46:10 2024

@author: motil
"""

def main():
    print("\n Operations Menu:\na or A: average \n* : multiplication \nm: minimum \nM : maximum \n^ : power \nq or Q : quit")
    ch=input("\nEnter a character :")
    while ch!='q' and ch!='Q':
        print("Enter two integer numbers.")
        n1=int(input("Enter the first integer:"))
        n2=int(input("Enter the second integer:"))
        if ch=='a' or ch=='A' :
                arg=(n1+n2)/2
                if (n1+n2)%2==0:
                    print("The average is:%.1f. It is an integer number."%(arg))
                elif (n1+n2)%2==1:
                    print("The average is:%.1f. It is not an integer number."%(arg))
        elif ch=='*':
            arg=n1*n2
            print("The multiplication is:%d"%(arg))
        elif ch=='m':
            if n1>n2 :
                print("The minimum is:",n2)
            else :
                print("The minimum is:",n1)
        elif ch=='M':
            if n1>n2:
                print("The maximum is:",n1)
            else:
                print("The maximum is:",n2)
        elif ch=='^':
            if n1==0 and n2<=0:
                print("Dividing by zero error")
            else:
                arg=n1**n2
                print("%d^%d is:%.2f"%(n1,n2,arg))
        print("\n Operations Menu:\na or A: average \n* : multiplication \nm: minimum \nM : maximum \n^ : power \nq or Q : quit")
        ch=(input("\n Enter a character :"))
    print("Finish")
main()

                
                
                
                
            
    
