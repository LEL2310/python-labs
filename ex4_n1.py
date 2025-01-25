# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:00:32 2025

@author: motil
"""

def is_palidrome(st,start,end):
    if start>=end:
        return True 
    return st[start]==st[end] and is_palidrome(st,start+1,end-1)


def is_in(st,lst_st,index):
    if index>=len(lst_st):
        return False 
    if lst_st[index]==st:
        return True 
    return is_in(st,lst_st,index+1)


def substring(st,pali_lst,start,end):
    if start>=len(st):
        return pali_lst
    if end>=len(st):
        return substring(st, pali_lst, start+1, start+1)
    sub=st[start:end+1]
    if is_palidrome(sub, 0, len(sub)-1) and not(is_in(sub, pali_lst, 0)):
        pali_lst.append(sub)
    return substring(st, pali_lst, start, end+1)
    

    
    
def num_of_palindromes(st,start,end,pali_lst):
    substring(st, pali_lst, start, end)
    return len(pali_lst)

 
    
    
def recursive_sts_lst_input(lst):
    ls=input()
    if ls=="":
        return lst
    lst.append(ls)
    return recursive_sts_lst_input(lst)


def main():
    lst=[]
    print("Please enter strings, separated by new lines. Enter an empty string for stop inputing: ")
    recursive_sts_lst_input(lst)
    for st in lst:
        palindromes_lst=[]
        print("The number of palindroms in'%s' is %d" %(st, num_of_palindromes(st, 0, 0, palindromes_lst)))
main()
   
    
    
    
    

    
   


