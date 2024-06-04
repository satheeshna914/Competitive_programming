#factorial using tabulation
def generate_factorial(n):
    if n==0:
        return 1
    fact_series=[0]*(n+1)
    fact_series[0]=1
    for i in range(1,n+1):
        fact_series[i]=fact_series[i-1]*i
        print(fact_series)
    return fact_series[n] 
n=int(input("Enter the number to calculate factorial:"))
print("Factorial of:",n,"is:",generate_factorial(n))
