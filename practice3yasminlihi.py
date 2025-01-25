# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:07:21 2025

@author: motil
"""
def lit_letters(str):
    l_letters=""
    for i in range(len(str)):
        if str[i]>='a' and str[i]<='z':
            l_letters+= str[i]
        elif  str[i]>='A' and  str[i]<='Z':
            lit=ord( str[i])+(ord('a')-ord('A'))
            l_letters+=chr(lit)
            
def count_occurrences(t,s):
    count=0
    len_t=len(t)
    len_s=len(s)
    for i in range(len_s-len_t+1):
        if s[i:i+len_t]==t:
            count+=1
    return count

            
def min_letter(str1,sub_str):
    str1=lit_letters(str)
    sub_str=lit_letters(sub_str)
    if str1[0]<sub_str[0]:
        return str1
    elif sub_str[0]<str1[0]:
        return sub_str
    else:
        for ch in str1:
            for ch1 in sub_str:
                if ch<ch1:
                    return str1
                elif ch1<ch:
                    return sub_str
                
def max_occurrences(s,lst):
    max=0
    w=""
    max_st1=""
    for i in range(len(lst)):
        c=count_occurrences(lst, s)
        if c>max:
            max=c
            w=str[i]
        elif c==max:
            max_st1=str[i]
            for i in range(len(max_st1)):
                w=min_letter(w,max_st1)
                return w
    return w
                
                
                
                
                
    
def main():
    str1=input("Enter a string:")
    length=int(input("Enter the list length:"))
    print("Enter %d strings:"%(length))
    ls_w=[]
    for i in range(length):
        ls_w.append(input())
    m_w=max_occurrences(str1,ls_w)
    print("The most repeated is ")
    print(m_w,end="")
    
main()