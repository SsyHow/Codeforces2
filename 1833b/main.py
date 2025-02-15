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
from collections import defaultdict
a = II()
for _ in range(a):
    b, c = MII()
    L1 = LII()
    L2 = LII()

    M1 = sorted(L1)
    L2.sort()
    k = defaultdict(list)
    for i in range(b):
        k[M1[i]].append(L2[i])

    for i in L1:
        print(k[i].pop(), end=' ')
    print()