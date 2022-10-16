#Memoization using list
def fibL(n, dp):
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return n

    if dp[n-1] == -1:
        ans1 = fibL(n-1, dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]

    if dp[n-2] == -1:
        ans2 = fibL(n-2, dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]


    return ans1 + ans2

#Memoizaton using dictionary
def fibD(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fibD(n-1, d) + fibD(n-2, d)
        d[n] = ans
        return ans

#Memoizaton using dictionary better
def fibDEfficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return n

    if n-1 not in d:
        ans1 = fibDEfficient(n-1, d)
        d[n-1] = ans1
    else:
        ans1 = d[n-1]

    if n-2 not in d:
        ans2 = fibDEfficient(n-2, d)
        d[n-2] = ans2
    else:
        ans2 = d[n-2]

    return ans1 + ans2

#Iterative DP
def fibI(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    i = 2
    while i <= n:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
    return dp[n], dp

#Iterative without memoization
# Space O(1)
def fibb(n):
    fib0 = 0
    fib1 = 1

    if n == 1:
        return fib1
    i = 2
    while i <= n:
        ans = fib0 + fib1
        fib0 = fib1
        fib1 = ans
        i += 1
    return ans

if __name__ == '__main__':
    n = int(input("Enter n: "))
    numFibCalls = 0
    dp = [-1 for i in range(n+1)]
    print(fibL(n, dp))
    print("No. of calls = ", numFibCalls)
    print(dp)

    numFibCalls = 0
    d = {0:0, 1:1}
    print(fibD(n, d))
    print("No. of calls = ", numFibCalls)
    print(d)

    numFibCalls = 0
    d = dict()
    print(fibDEfficient(n, d))
    print("No. of calls = ", numFibCalls)
    print(d)

    ans, dp = fibI(n)
    print(ans)
    print(dp)

    print(fibb(n))
