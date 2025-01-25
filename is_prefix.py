# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:34:40 2025

@author: motil
"""
#checks if the pre string is prefix for the  string 
def is_prefix(p_st,st):
    if len(p_st)==0:
        return False
#checks that the pre string is not longer then the string 
    if len(p_st)>len(st):
        return False
    if p_st[0]!=st[0]:
        return False
    if len(p_st)==1 and p_st[0]==st[0]:
        return True  
#checks the next char every time
    return is_prefix((p_st[1:]), (st[1:]))
    
def main():
    st=input("Enter a string:")
    pre_str=input("Enter another string:")
    if is_prefix(pre_str, st):
        print("%s is a prefix of %s"%(pre_str,st))
    else:
        print("%s is not a prefix of %s"%(pre_str,st))
main()