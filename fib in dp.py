def fib(n):
    if n<=1:
        return n
    if memo[n]!=0:
        return memo[n]
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
n=int(input())
memo=[0]*(n+1)
memo[0]=0
memo[1]=1
print(fib(n),memo)