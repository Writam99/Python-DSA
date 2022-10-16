#Recursive
def knapsack(W, val, wt, n, i):
    if i == n:
        return 0

    if wt[i] > W:
        ans = knapsack(W, val, wt, n, i + 1)
    else:
        ans1 = val[i] + knapsack(W - wt[i], val, wt, n, i + 1)
        ans2 = knapsack(W, val, wt, n, i + 1)
        ans = max(ans1, ans2)
    return ans

#Iterative Memoization
def knapsackI(W, val, wt):
    n = len(val)
    dp = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(W+1):
            if j < wt[i-1]:
                ans = dp[i-1][j]
            else:
                ans1 = val[i-1] + dp[i-1][j - wt[i-1]]
                ans2 = dp[i-1][j]
                ans = max(ans1, ans2)
            dp[i][j] = ans

    return dp[n][W]

if __name__ == '__main__':
    val = [200, 300, 100]
    wt = [20, 25, 30]
    W = 50
    n = len(val)
    ans = knapsack(W, val, wt, n, 0)
    print(ans)

    print('---------------------------------')

    ans = knapsackI(W, val, wt)
    print(ans)

