def coinchange(coins,amount):
    dp=[0]*(amount+1)
    for i in coins:
        for j in range(i,amount+1):
            dp[j]=1+dp[j-i]
    print(dp)
    return dp[amount]
coins=[1,2,5]
amount=11
coinchange(coins,amount)