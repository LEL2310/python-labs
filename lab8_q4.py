# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:40:33 2025

@author: motil
"""
#takes each word in a stentence and write it in a seperate row
def drop_row(str):
    words=[]
    c_word=""
    for ch in str:
#checks if there is a tab or space if there is it means the word ends 
        if ch == " " or ch == "\t":
            if c_word!="":
                words.append(c_word)
                c_word=""
            else:
#Does'nt matter how many spaces there are it drops just one row 
                if ch!=" ":
                    c_word+=ch
        else:
            c_word+=ch
#Writes the last word even if there isnt a space or tab 
    if c_word!=" ":
        words.append(c_word)
        
    for x in words:
        print(x)  
#Asks from the user a string as long as the stirng isnt emp
def main():
    flag=True
    while flag==True:
        st1=input("Enter a string, please:")
        if st1=="":
            print("finish")
            flag=False
        else:
            drop_row(st1)
            
main()
        
        
                
                
                    
            
        