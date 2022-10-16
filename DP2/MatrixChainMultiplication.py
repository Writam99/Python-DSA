import sys

#Recursive
def mcm(p, i, j):
    global numCalls
    numCalls += 1
    if i == j:
        return 0

    min_value = sys.maxsize
    for k in range(i, j):
        ans1 = mcm(p, i, k)
        ans2 = mcm(p, k+1, j)

        mCost = p[i-1]*p[k]*p[j]
        curr_value = ans1 + ans2 + mCost
        min_value = min(min_value, curr_value)
    return min_value

#Recursive Memoization
def mcmM(p, i, j, dp):
    global numCalls
    numCalls += 1
    if i == j:
        return 0

    min_value = sys.maxsize
    for k in range(i, j):
        if dp[i][k] == -1:
            ans1 = mcmM(p, i, k, dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]

        if dp[k+1][j] == -1:
            ans2 = mcmM(p, k + 1, j, dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]

        mCost = p[i - 1] * p[k] * p[j]
        curr_value = ans1 + ans2 + mCost
        min_value = min(min_value, curr_value)
    return min_value

if __name__ == '__main__':
    p = [22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
    n = len(p) - 1
    numCalls = 0
    ans = mcm(p,1,n)
    print('Ans =', ans)
    print('No. of calls =', numCalls)

    print('--------------------------')

    dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]
    numCalls = 0
    ans = mcmM(p,1,n,dp)
    print('Ans =', ans)
    print('No. of calls =', numCalls)
