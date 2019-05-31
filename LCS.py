"""

https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

Longest Common Subsequence

AGGTAB
GXTXAYB     ans : 4


"""


def lcs(a, b):
    n = len(a)
    m = len(b)

    dp = [[0]*(m+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            elif a[i-1] != b[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[n][m])

    return dp


def printLCS(dp, a, b, m, n):
    idx = dp[m][n] + 1
    lcs = [""]*idx
    i = m
    j = n
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
            lcs[idx-1] = a[i-1]
            i -= 1
            j -= 1
            idx -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    dp = lcs(a, b)

    m = len(a)
    n = len(b)

    print(printLCS(dp, a, b, m, n))
