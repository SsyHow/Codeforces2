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
from math import gcd
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    x, y = MII()
    if x & 1 == y & 1 == 0:
        k = y // 2
        print(x * k + 2)
    elif x & 1 == y & 1 == 1:

        print(x * y + 1)
    elif x & 1 == 1 and y & 1 == 0:
        if y % 4 > 0:
            print(-1)
        else:
            k = y // 2
            print(x * k + 2)
    else:
        print(-1)