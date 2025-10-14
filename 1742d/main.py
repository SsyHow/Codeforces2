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
from math import gcd
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    b = II()
    L = LII()
    k = [0] * 1001

    for idx, i in enumerate(L, start=1):
        k[i] = max(k[i], idx)
    ans = -1
    for i in range(1, 1001):
        for j in range(1, 1001):
            if k[i] and  k[j] and  gcd(i, j) == 1:
                ans = max(ans, k[i] + k[j])

    print(ans)