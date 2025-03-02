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
from collections import Counter

for _ in range(II()):
    b = II()
    c = Counter(MII())
    n, m = 0, 0
    f2 = f1 = True
    for i in range(100):
        if f2 and c[i] < 2:
            f2 = False
            n = i
        if f1 and c[i] < 1:
            f1 = False
            m = i
        if not f1 and not f2:
            break
    if f2:
        n = i + 1
    if f1:
        m = i + 1
    print(n +  m)