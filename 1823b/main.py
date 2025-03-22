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
a = II()
for _ in range(a):
    b, c = MII()
    L = LII()
    k = []
    for idx, i in enumerate(L,start=1):
        if idx % c != i % c:
            k.append(idx%c)
            k.append(i%c)
    c = Counter(k)
    l = c.items()
    if len(c) == 0:
        print(0)

    elif len(c) == 2 and all(c[i] == 2 for i in c):
        print(1)
    else:
        print(-1)
