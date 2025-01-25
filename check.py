# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:00:33 2025

@author: motil
"""

    n=len(mat)
    check_ls=[0]*(n)
    for i in range(n):
        if n[i]>n or n[i]<1:
            return False
        elif n[i]<=n:
            num=mat[i]
            check_ls[num]+=1
        for j in range (n+1):
                if n[j]>n:
                    return False
                elif n[j]<=n:
                    num=n[j]
                    check_ls[num]+=1
        if check_ls[num]>1:
            return False
        else:
            check_ls[num]=0
    return True