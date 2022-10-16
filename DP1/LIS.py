#Recursive
def lis(li, i, n):
    global numCalls
    numCalls += 1
    if i == n:
        return 0, 0
    including_max = 1
    for j in range(i+1, n):
        if li[j] >= li[i]:
            further_including_max = lis(li, j, n)[0]
            including_max = max(including_max, 1 + further_including_max)

    excluding_max = lis(li, i + 1, n)[1]
    overallMax = max(including_max, excluding_max)
    return including_max, overallMax

#Recursive memoization
def lisM(li, i, n, dp):
    global numCalls
    numCalls += 1
    if i == n:
        return 0, 0

    including_max = 1
    for j in range(i + 1, n):
        if li[j] >= li[i]:
            if dp[j] == -1:
                ans = lisM(li, j, n, dp)
                dp[j] = ans
                further_including_max = ans[0]
            else:
                further_including_max = dp[j][0]
            including_max = max(including_max, 1 + further_including_max)

    if dp[i+1] == -1:
        ans = lisM(li, i + 1, n, dp)
        dp[i+1] = ans
        excluding_max = ans[1]
    else:
        excluding_max = dp[i+1][1]
    overallMax = max(including_max, excluding_max)
    return including_max, overallMax

#Iterative Memoization(Strictly Increasing)
def lisI(li, n):
    dp = [[0 for j in range(2)] for i in range(n+1)]

    for i in range(n-1, -1, -1):
        including_max = 1
        for j in range(i+1, n):
            if li[j] > li[i]:
                including_max = max(including_max, 1 + dp[j][0])

        dp[i][0] = including_max
        excluding_max = dp[i+1][1]
        overallMax = max(including_max, excluding_max)
        dp[i][1] = overallMax

    return dp[0][1]

if __name__ == '__main__':
    n = int(input("Enter n: "))
    li = [int(ele) for ele in input().split()]
    dp = [-1 for _ in range(n+1)]
    numCalls = 0
    ans = lis(li, 0, n)[1]
    print(ans)
    print("Calls =", numCalls)
    print('-----------------------------')

    numCalls = 0
    ans = lisM(li, 0, n, dp)[1]
    print(ans)
    print("Calls =", numCalls)

    print('-----------------------------')
    ans = lisI(li, n)
    print(ans)