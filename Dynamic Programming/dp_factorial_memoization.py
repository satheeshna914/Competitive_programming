# find n factorial using memoization - recursive approach

def factorial(n,memo={}):
    if n in memo:
        return memo[n]#if it already exists returns it
    if n<=1:
        return 1#base case
    memo[n]=n*factorial(n-1,memo)#computes and adds to the memo suppose fact(5) memo[5]=5*fact(5-1,memo) ->memo[5]=5*fact(4,memo)"means result of fact(4) which is already computed so it directly multiplies 5 with result of fact(4) that is 5*24=120
    print("N:",n,"Memo:",memo)
    return memo[n]
n=int(input("Enter the number to calculate factorial:"))
print("factorial of ",n,"is:",factorial(n))
