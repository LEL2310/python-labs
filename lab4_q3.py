# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:29:24 2024

@author: motil
"""

def main():
    C=int(input("Number of children:\n"))
    salary=int(input("Monthly salary:\n"))
    sr=input("Military, or civil service(enter character Y, or y for yes, otherwise any other character)?\n")
    if salary>=17500:
        print("The mortgage is approved with monthly payment of %.2f."%(salary*0.35))
    elif C>=5 and salary>=14000:
        print("The mortgage is approved with monthly payment of %.2f."%(salary*0.25))
    elif (sr=="Y" or sr=="y") and salary>=15000:
        print("The mortgage is approved with monthly payment of %.2f."%(salary*0.25))
    else:
        print("Sorry, the mortgage is not approved.")
main()