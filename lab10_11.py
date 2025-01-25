# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:45:51 2025

@author: motil
"""
#checks if the string has only letters
def all_letters(str):
    if str=="":
        return True
    if str[0]>='a' and str[0]<='z' or str[0]>='A' and str[0]<='Z':
#if it's a letter checks the next letter
        return all_letters(str[1:])
    return False


def main():
    str=input("Please enter a string:")
    if all_letters(str):
        print("The string is legal.")
    else:
        print("The string is illegal!")
main()

