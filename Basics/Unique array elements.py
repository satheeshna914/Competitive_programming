'''Eliminate repeated letters in Array. Printing non repeating elements in array and 
printing the total. 
Arr1 = {1,2,3,4,5} Len1 = 5 
Arr 2 = {2,6,8,10} Len2 = 4 
Output = {1,3,4,5,6,8,10} Total is 7'''
def mcode(arr1,arr2):
    s=[]
    for i in arr1:
        if i not in arr2:
            s.append(i)
    for j in arr2:
        if j not  in arr1:
            s.append(j)
    return s, len(s)
arr1=[1,2,3,4,5]
arr2=[2,6,8,10]
print(mcode(arr1,arr2))
 
 #2nd method------------
def unique(arr1,arr2):
    return list(set(arr1) ^ set(arr2)), len(list(set(arr1) ^ set(arr2)))
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(unique(arr1,arr2))
