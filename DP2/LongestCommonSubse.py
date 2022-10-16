#Longest Common Subsequence

#Recursive
def lcs(s1, s2, i, j):
    global numCalls
    numCalls += 1
    if i == len(s1) or j == len(s2):
        return 0

    if s1[i] == s2[j]:
        ans = 1 + lcs(s1, s2, i + 1, j +1)
    else:
        ans1 = lcs(s1, s2, i + 1, j)
        ans2 = lcs(s1, s2, i, j +1)
        ans = max(ans1, ans2)

    return ans

#Recursive Memoization
def lcsM(s1, s2, i, j, dp):
    global numCalls
    numCalls += 1
    if i == len(s1) or j == len(s2):
        return 0

    if s1[i] == s2[j]:
        if dp[i+1][j+1] == -1:
            smallAns = lcsM(s1, s2, i + 1, j +1, dp)
            dp[i + 1][j + 1] = smallAns
            ans = 1 + smallAns
        else:
            ans = 1 + dp[i+1][j+1]
    else:
        if dp[i + 1][j] == -1:
            ans1 = lcsM(s1, s2, i + 1, j, dp)
            dp[i + 1][j] = ans1
        else:
            ans1 = dp[i + 1][j]

        if dp[i][j + 1] == -1:
            ans2 = lcsM(s1, s2, i, j +1, dp)
            dp[i][j + 1] = ans2
        else:
            ans2 = dp[i][j + 1]

        ans = max(ans1, ans2)

    return ans

#Iterative Memoizatiob
def lcsI(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):

            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]


if __name__ == '__main__':
    s1 = 'abedgjc'
    s2 = 'bmdgsc'
    numCalls = 0
    ans = lcs(s1, s2, 0, 0)
    print('Ans =',ans)
    print('No. of  calls =', numCalls)

    print('---------------------------------------')

    n = len(s1)
    m = len(s2)
    dp = [[-1 for j in range(m+1)] for i in range(n+1)]
    numCalls = 0
    ans = lcsM(s1, s2, 0, 0, dp)
    print('Ans =',ans)
    print('No. of  calls =', numCalls)

    print('---------------------------------------')

    print('Ans =', lcsI(s1, s2))