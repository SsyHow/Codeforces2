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

    ans = 0
    for i in L:
        ans = gcd(ans, i)

    if ans == 1:
        print(0)
    elif gcd(ans, b) == 1:
        print(1)
    elif gcd(ans, b - 1) == 1:
        print(2)
    else:
        print(3)