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
from math import gcd
a = II()
for _ in range(a):
    b = II()
    L = LII()
    ans = 0
    for i in range(b):
        if L[i] - 1 - i == 0:
            continue
        ans = gcd(ans, abs(L[i] - 1 - i))
    print(ans)