import sys

input = lambda: sys.stdin.readline().rstrip()


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
a = II()
for _ in range(a):
    n, m = MII()
    L = []
    row = [0] * n
    col = [0] * m
    for i in range(n):
        k = I()
        L.append(k)
        for j in range(m):
            if k[j] == '.':
                row[i] += 1
                col[j] += 1

    ans = n + m - 1
    for i, r in enumerate(row):
        for j, c in enumerate(col):
            ans = min(ans, r + c - int(L[i][j] == '.'))
    print(ans)