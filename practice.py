# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:53:35 2024

@author: motil
"""

def main():
    g=input("Please enter your gender(enter M for male, F for female)")
    a=int(input("Please enter your age:"))
    b=input("Do you have a bagrut? (enter Y for yes and N for no )")
    if g=='F' and a>=20 and b=='Y':
        print("Allow")
    elif g=='M' and a>=21 and b=='Y':
        print("Allow")
    else:
        print("Not allow")
main()
