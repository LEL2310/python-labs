# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:04:59 2024

@author: motil
"""
#Calculate the average time 
def my_avg(L):
    sum=0
    for i in range(len(L)):
        sum+=L[i]
    avg_sum=sum/len(L)
    return avg_sum
#Count the number of runners that their time below the avg time
def count_below_avg(L,avg):
    count=0
    for i in range(len(L)):
        if L[i]<avg:
            count+=1
    return count
def main():
    L=[]
    n=int(input("Enter number of runners:"))
    list=n+1
    while n!=0:
        t=float(input("%d Enter time:"%(list-n)))
        L.append(t)
        n-=1
    avg=my_avg(L)
    print("Time average is %.2f."%avg)
    new=count_below_avg(L, avg)
    print("The number of runners, running below average time is %d."%new)
main()