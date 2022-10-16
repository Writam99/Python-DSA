import sys

#Recursive
def minCost(cost, i, j, n , m):
    global numCalls
    numCalls += 1
    #Special case
    if i == n -1 and j == m -1:
        return cost[i][j]

    #Base case
    if i >= n or j >= m:
        return sys.maxsize

    ans1 = minCost(cost, i + 1, j, n, m)
    ans2 = minCost(cost, i, j + 1, n, m)
    ans3 = minCost(cost, i + 1, j + 1, n, m)

    ans = cost[i][j] + min(ans1, ans2, ans3)
    return ans

#Recursive memoization using list
def minCostRL(cost, i, j, n , m, dp):
    # print('(' + str(i) + ',' + str(j) + ')', end = '')
    global numCalls
    numCalls += 1
    # Special case
    if i == n - 1 and j == m - 1:
        return cost[i][j]

    # Base case
    if i >= n or j >= m:
        return sys.maxsize

    if dp[i+1][j] == sys.maxsize:
        ans1 = minCostRL(cost, i + 1, j, n, m, dp)
        dp[i + 1][j] = ans1
    else:
        ans1 = dp[i+1][j]

    if dp[i][j+1] == sys.maxsize:
        ans2 = minCostRL(cost, i, j + 1, n, m, dp)
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1]

    if dp[i+1][j+1] == sys.maxsize:
        ans3 = minCostRL(cost, i + 1, j + 1, n, m, dp)
        dp[i + 1][j + 1] = ans3
    else:
        ans3 = dp[i+1][j+1]

    ans = cost[i][j] + min(ans1, ans2, ans3)
    return ans

#Recursive memoization using dictionary
def minCostRD(cost, i, j, n , m, dp = {}):
    # print('(' + str(i) + ',' + str(j) + ')', end = '')
    global numCalls
    numCalls += 1
    # Special case
    if i == n - 1 and j == m - 1:
        return cost[i][j]

    # Base case
    if i >= n or j >= m:
        return sys.maxsize

    if (i + 1, j) not in dp:
        ans1 = minCostRD(cost, i + 1, j, n, m, dp)
        dp[(i + 1, j)] = ans1
    else:
        ans1 = dp[(i + 1, j)]

    if (i, j +1) not in dp:
        ans2 = minCostRD(cost, i, j + 1, n, m, dp)
        dp[(i, j +1)] = ans2
    else:
        ans2 = dp[(i, j +1)]

    if (i + 1, j + 1) not in dp:
        ans3 = minCostRD(cost, i + 1, j + 1, n, m, dp)
        dp[(i + 1, j + 1)] = ans3
    else:
        ans3 = dp[(i + 1, j + 1)]

    ans = cost[i][j] + min(ans1, ans2, ans3)
    return ans

#Iterative memoization
def minCostIterative(cost, n, m):
    dp = [[sys.maxsize for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                dp[i][j] = cost[i][j]
            else:
                ans1 = dp[i+1][j]
                ans2 = dp[i][j+1]
                ans3 = dp[i+1][j+1]
                dp[i][j] = cost[i][j] + min(ans1, ans2, ans3)

    return dp[0][0]


if __name__ == '__main__':
    cost = [[1,5,11], [8,13,12], [2,3,7], [15,16,18]]

    # numCalls = 0
    # ans = minCost(cost, 0, 0, 4, 3)
    # print('Ans = ', ans)
    # print('No. of  calls =', numCalls)



    n = 4
    m = 3
    # dp = [[sys.maxsize for _ in range(m+1)] for _ in range(n+1)]
    # numCalls = 0
    # ans = minCostRL(cost, 0, 0, 4, 3, dp)
    # print('Ans = ', ans)
    # print('No. of  calls =', numCalls)

    # numCalls = 0
    # ans = minCostRD(cost, 0, 0, 4, 3)
    # print('Ans = ', ans)
    # print('No. of  calls =', numCalls)

    ans = minCostIterative(cost, 4, 3)
    print(ans)