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
    g = 0
    Kt = 0
    b = II()
    for i in MII():
        g = gcd(g, i)
        Kt = max(Kt, i)
    print(Kt // g)