#fibonacci using tabulation
def generate_fib_series(n):
    fib_series=[0]*(n+1)#list with all zeros of n+1 times and at end of result it returns from 1:
    fib_series[1]=1#base case
    for i in range(2,n+1):
        fib_series[i]=fib_series[i-1]+fib_series[i-2]#returns the values using indexes of the fib_series list
        print(fib_series)#returns the list at every iteration
    return fib_series[1:]#returns the final result (it is given out of the loop) here we use [1:] because we ignore 0 case 
n=int(input("Enter the number of fibonacci numbers you want to generate:"))
fib_series=generate_fib_series(n)
print("The first",n,"Fibonacci numbers are:",fib_series)
