
def minCostClimbingStairs( cost):
    n=len(cost)
    memo=[-1]*(n)
    memo[0]=cost[0]
    memo[1]=cost[1]
    def top_down(n):
        if memo[n]!=-1:
            return memo[n]
        memo[n]=cost[n]+min(top_down(n-1),top_down(n-2))
        return memo[n]
    return min(top_down(n-1),top_down(n-2))
a=minCostClimbingStairs([10,15,20])
print(a)