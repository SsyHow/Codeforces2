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
t = II()
for _ in range(t):
    n, k, a, b = MII()
    L = []
    for _ in range(n):
        L.append(LII())

    K = L[:k]
    x = L[a - 1]
    y = L[b - 1]
    disx = 0 if a <= k else 1 << 60
    disy = 0 if b <=k else 1 << 60

    for i in K:
        if disx:
            disx = min(disx, abs(i[0] - x[0]) + abs(i[1] - x[1]))
        if disy:
            disy = min(disy, abs(i[0] - y[0]) + abs(i[1] - y[1]))

    print(min(abs(y[0] - x[0]) + abs(y[1] - x[1]), disx + disy))

