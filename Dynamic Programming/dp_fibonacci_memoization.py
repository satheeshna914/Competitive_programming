#memoization is used in recursive approach
def fib(n,memo={}):#here we are using a default function parameter memo dict
    if n in memo:
        return memo[n]#directly calls if it is already computed from cache i.e, dict{}
    if n<=2:
        return 1#This i s a base case 
    print("N=",n,"Memo=",memo)
    memo[n]=fib(n-1,memo)+fib(n-2,memo)#dict key values are stored
    return memo[n]
def generate_fib_series(n):
    fib_series=[]
    for i in range(1,n+1):
        fib_series.append(fib(i))
    return fib_series
n=int(input("Enter the number of fibonacci numbers you want to genrate:"))
fib_series=generate_fib_series(n)
print("the first",n,"Fibonacci numbers are",fib_series)
