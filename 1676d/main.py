def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from collections import defaultdict
t = II()
for _ in range(t):
    n, m = MII()
    L = []
    for _ in range(n):
        L.append(LII())
    X = defaultdict(int)
    Y = defaultdict(int)
    for i in range(n):
        for j in range(m):
            X[i - j] += L[i][j]
            Y[i + j] += L[i][j]
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, X[i - j] + Y[i + j] - L[i][j] )

    print(ans)