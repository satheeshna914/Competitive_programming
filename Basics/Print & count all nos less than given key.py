 #Print and count all the numbers which are less than a given key element from a given array. 
def count_numbers(arr, key):
    c=0
    res=[]
    for i in arr:
        if i<=key:
            res.append(i)# or print(i.end="")
            c+=1
    return c,res
arr=list(map(int,input().split()))
key=int(input())
print(count_numbers(arr,key))

# -----------direct approach--------

def count_numbers(arr, key):
    return len([i for i in arr if i<=key]),[i for i in arr if i<=key]
arr=list(map(int,input().split()))  # 1 2 3 4 5 6 7 8 9 10
key=int(input())  # 5       # 5 4 3 2 1
print(count_numbers(arr,key))  # (5, [1, 2, 3, 4, 5])   
