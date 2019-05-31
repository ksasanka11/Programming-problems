"""
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits
(operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.


str1 = "sunday"
str2 = "saturday"
ans : 3
"""


def naive(s1, s2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if s1[m-1] == s2[n-1]:
        return naive(s1, s2, m-1, n-1)

    return 1 + min(
            naive(s1, s2, m, n-1),  # insert
            naive(s1, s2, m-1, n),  # delete
            naive(s1, s2, m-1, n-1)
    )


# dp
def editDistace(s1, s2, m, n):
    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[m][n] 


if __name__ == "__main__":
    s1 = input().strip()
    s2 = input().strip()
    m = len(s1)
    n = len(s2)
    print(editDistace(s1, s2, m, n))
