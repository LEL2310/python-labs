# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:19:08 2024

@author: motil
"""

def main(): 
    start=0
    s_start=0
    s_delta=0
    delta=0
    length=0
    s_length=0
    f_num=int(input("Insert 1st number:"))
    while f_num!=-1 and f_num>0:
        s_num=int(input("Insert next number, end with -1:"))
        if s_num==-1 or s_num<=0:
            f_num=s_num
        else:
            if delta!=s_delta:
                length=s_length-1
                delta=s_delta
            else:
                s_num-f_num==s_delta
                s_length+=1
            if s_length>length:
                length=s_length
               s_start=f_num
            s_delta=s_num-f_num
    if (f_num!=-1 and f_num<=0):
        print("Illigal number")
    print("Longest mathematical series start with %d, delta of %d, length of %d"%(start,delta,length))
    


main()
        
        
        
        

                
                    
                    
            
                
        
    
            
            
        
            
        
       
            
       
    

        
            