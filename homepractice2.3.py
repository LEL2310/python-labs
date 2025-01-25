

def build_list():
    series=int(input("Enter integer numbers > 0, end with -1:"))
    a=[series]
    while series != -1:
        series=int(input())
        a.append(series)
    return a 
def sep_list(num):
    sep=[]
    while num!=0:
        sep.append(num%10)
        num//=10
    return sep
def reverse(ls):
    length=len(ls)
    for i in range(length//2):
        ls[i],ls[length-i-1]=ls[length-i-1],ls[i]
    return ls


def f_num(lst):
    le = len(lst)
    f_n = 0
    for i in range(le):
        f_n += lst[i]*10**(le-1-i)
    return(f_n)

def print_list(a):
    for i in range(len(a)):
        print(a[i], end="")
        if i<len(a)-1:
            print(",", end="")
    print()

   
def clock_wise_shift(a):
    num_list=sep_list(a)
    rev_list=reverse(num_list)
    length=len(rev_list)
    for i in range(1,length):
        rev_list[i-1], rev_list[i] = rev_list[i], rev_list[i-1]
    return rev_list
#m=move n=the primary list
def clock_wise_shift_n(n,m):
    n_list = n
    for i in range(m):
       n_list = clock_wise_shift(n_list)
    return n_list
def shift_all(a):
    new_list=[]
    for i in range(len(a)):
        n_num=clock_wise_shift_n(sep_list(a[i]),i)
        n_num = f_num(n_num)
        new_list.append(n_num)
    return new_list
def main():
    before=build_list()
    print("The initial list is:", end="")
    print_list(before)
    after=shift_all(before)
    print("The list after it's items clockwise shifting is: ", end="")
    print_list(after)

main()  
    
    

            
        


       
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  

