def odd(n):
    if n==11:
        return 
    if n%2!=0:
        print(n)
    odd(n+1)
n=int(input())
result=odd(n)
print(result)