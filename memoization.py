count=0
n=int(input())
memo=[0]*(n+1)
def fib(n):
    global count
    if n==0 or n==1:
        count=count+1
        return n
    if memo[n]!=0:
        count=count+1
        return memo[n]
    count=count+1
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
result=fib(n)
print(result,count)
    
