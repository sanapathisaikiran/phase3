n=int(input())
count=0
memo=[0]*(n+1)
memo[1]=1
def fib(n):
    global count
    for i in range(2,n+1):
        memo[i]=memo[i-1]+memo[i-2]
        count=count+1
result=fib(n)
print(result,count)