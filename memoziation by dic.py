memo={}
def fib(n):
    global memo
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
n=int(input())
result=fib(n)
print(result,memo)