# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:06:10 2024

@author: motil
"""
#ליהי אליאס:319041109
#יסמין אסקרוב:323017012

#Checks if a natural num belongs to the group 
def belong(group,number):
    for i in group:
        if number==i:
            return True
    return False
#Build a list of numbers that apears both in the first froup and the second one
def intersect(group1,group2):
    set=[]
    for x in group1:
        if x in group2:
            set.append(x)
    return set
#Build a list of numbers both from group1&group2 but doesnt repeats on the same number
def unify(group1,group2):
    union=[]
    for x in group1:
        if x not in union:
            union.append(x)
    for x in group2:
        if x not in union:
            union.append(x)
    return union
#Checks if there are numbers that apears both in group1&2  
def is_subset(group1,group2):
    for num in group1:
        if num not in group2:
            return False
    return True
#Check if the groups if group A contain group B and and opposite
def are_equal(A,B):
    sub1=is_subset(A,B)
    sub2=is_subset(B,A)
    if sub1==sub2:
        return True
    else:
        return False
#Build a list of the difference between A and B
def difference(A,B):
    diff=[]
    for num in A:
        if num not in B:
            diff.append(num)
    return diff
#Returns the symmetric difference 
def sym_diff(A,B):
    diff_A_B = difference(A, B)
    diff_B_A = difference(B, A)
    return unify(diff_A_B, diff_B_A)
#Build and returns a group of right numbers 
def build_set():
    n=int(input())
    A=[]
    if n==0:
       return A 
    print("Enter %d natural numbers between 1 to 100, with no repetitions"%(n))
    len=0
#The loop works till there are n right numbers 
    while len<n:
        num=int(input())
#checks that the number are on the scale
        if num<1 or num>100:
            print ("Wrong input")
            num=int(input())
#Checks that there are no equal numbers
        if num in A:
            print("Wrong input")
            num=int(input())
        A.append(num)    
        len+=1
    return A
#Build a list from 1-100
def build_universal():
    U=[]
    for i in range (1,101):
        U.append(i)
    return U
#checks if the list is empty
def is_empty(group):
    grou=[]
    if len(group)!=0:
        return False
    return True
#checks if the list is equal to the universal list(1-100)
def is_universal(group):
    uni=build_universal()
    equal=are_equal(uni,group)
    return equal
def main ():
    print("Enter the size of set A ")
    A=build_set()
    print("A set is",A)
    print("\nEnter the size of set B ")
    B=build_set()
    print("B set is",B)
    number=int(input("\nEnter a natural number:"))
    bel1=belong(A,number)
    bel2=belong(B,number)
    #Checks which messege to show
    if bel1==True or bel2==True:
        print("\n%d belongs to A or to B"%(number))
    else:
        print("\n%d doesn't belong either to A or B "%(number))
    cut=intersect(A,B)
    emp1=is_empty(cut)
    if emp1!=True:
        print("The intersection of A and B is",cut)
    else:
        print("The intersection of A and B is empty")
    uni=unify(A,B)
    emp2=is_empty(uni)
    if emp2!=True:
        print("The union of A and B is:", uni)   
    else:
        print("The union of A and B is empty")
    diff=sym_diff(A, B)
    emp3=is_empty(diff)
    if emp3!=True:
        print("The symmetric difference of A and B is:", diff)   
    else:
        print("The symmetric difference of A and B is empty")
    universal=is_universal(uni)
    if universal==False:
        print("A union B is not equal to universal set")
        
main()
    
    
    
    
        
    
    
    


            
        
        
        
    
    

        

    