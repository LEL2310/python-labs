# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:48:43 2024

@author: motil
"""

import math 
def height(v,a,t):
    g=9.81
    height=v*math.sin(deg2rad(a))*t-(g*(t**2)/2)
    return height
def horizontal(v,a,t):
    horizon=v*math.cos(deg2rad(a))*t
    return horizon 
def deg2rad(a):
    a_rad=(a*math.pi)/180
    return a_rad
def main():
    v=0
    a=0
    #Checking the terms for the loop to work 
    while v!=-1 and a!=-1:
        v,a=eval(input("Enter v(0-100) m/s and a(0-90 degrees):"))
        t=0
        if v>=0 and v<=100 and a>=0 and a<=90:
            he=0
            s=0
            #Calculate the height and distance as long as it not fallen 
            while he>=0:
                t+=0.1
                he=height(v, a, t)
                s=horizontal(v, a, t)
                print ("Time: %.1f.....S=%5.2f H=%5.2f ......"%(t,s,he))
            print("Fallen\n")
        else:
            v=-1
            a=-1
    print("Finish")
            
    
main()

            
        
            
        
    
