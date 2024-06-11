count=0
def fib(n):
    global count
    if n==1 or n==0:
        count=count+1
        return n
    count=count+1
    return fib(n-1)+fib(n-2)
n=int(input())
result=fib(n)
print(result,count)