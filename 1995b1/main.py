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
from collections import defaultdict
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    n, m = MII()
    a = LII()
    hs = {}
    for x in a:
        if x not in hs:
            hs[x] = 0
        hs[x] += 1
    ans = 0
    for x in hs:
        y = hs[x]
        l = min(m // x, y)
        ans = max(ans, l * x)
        if x + 1 not in hs:
            continue
        z = hs[x + 1]
        for i in range(1, y + 1):
            if i * x > m:
                break
            du = m - i * x
            su = min(du // (x + 1), z) * (x + 1) + i * x
            ans = max(su, ans)
    print(ans)