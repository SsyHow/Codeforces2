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
from bisect import bisect_left
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    m, n = MII()
    L = LII()
    L.sort(reverse=True)
    for i in range(1, m):
        L[i] += L[i - 1]

    # print(L)

    for _ in range(n):
        b = II()
        k = bisect_left(L, b)
        print(k + 1 if k != m else -1)
