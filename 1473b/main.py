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
from math import lcm
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    s1 = I()
    s2 = I()

    l1 = len(s1)
    l2 = len(s2)
    k = lcm(l1, l2)
    if s1 * (k // l1) != s2 * (k // l2):

        print(-1)
    else:
        print(s1 * (k // l1))

