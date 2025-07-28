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
from collections import *
a = II()
for _ in range(a):
    _, k = MII()
    L = Counter(I().split())
    m = len(L)
    for i in sorted(L.values()):
        if k < i:
            break
        k -= i
        m -= 1
    print(max(1, m))
