def minStepsTo1(n, dp):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 0

    ans1 = float("inf")
    if n % 3 == 0:
        if dp[n//3] == -1:
            ans1 = minStepsTo1(n//3, dp)
            dp[n//3] = ans1
        else:
            ans1 = dp[n//3]

    ans2 = float("inf")
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minStepsTo1(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]

    if dp[n-1] == -1:
        ans3 = minStepsTo1(n -1, dp)
        dp[n-1] = ans3
    else:
        ans3 = dp[n-1]

    ans = 1 + min(ans1, ans2, ans3)
    return ans

#Iterative
def minStepsI(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 0
    for i in range(2, n + 1):
        ans1 = dp[i-1]
        ans2 = (dp[i//2] if i % 2 == 0 else float("inf"))
        ans3 =  (dp[i//3] if i % 3 == 0 else float("inf"))
        dp[i] = 1 + min(ans1, ans2, ans3)

    return dp[n]

if __name__ == '__main__':
    n = int(input("Enter n: "))
    dp = [-1 for i in range(n+1)]
    numFibCalls = 0
    print('ans = ', minStepsTo1(n, dp))
    print("No. of calls = ", numFibCalls)

    print("Iterative:")
    print('ans = ', minStepsI(n))
