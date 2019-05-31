"""

Longest Increasing Subsequence

lis[i] : length of lis ending at i including i

Base case : lis[0...n-1] = 1


condition lis[i] < lis[j] + 1 :
That is because if we have already found a longer increasing subsequence(lis[i]) than that obtained by just tacking
on another character (lis[j] + 1) then that tacking on operation will not yield the LIS eventually.

"""


def lis():
    a = list(map(int, input().split()))
    n = len(a)
    lis = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if a[j] < a[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    ans = max(lis)
    print(ans)
    print(a)
    print(lis)


if __name__ == "__main__":
    lis()
