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
    n, x, k = MII()
    L = LII()
    L.sort()
    for i in range(1, n):
        L[i] += L[i - 1]
    zz = - 1<< 60
    for i in range(x + 1):
        j = n - i
        xx = L[j - k - 1] if j - k - 1 >= 0 else 0
        yy = L[j - 1] if j - 1 >= 0 else 0
        zz = max(zz, xx * 2 - yy)
    print(zz)