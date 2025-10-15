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
from collections import Counter
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    b = II()
    L = LII()

    c = sorted(Counter(L).items(), key = lambda x: -x[1])
    if len(c) == 1 and c[0][1] == 1:
        print(0)
        continue

    print(max(min(c[0][1], len(c) - 1), min(c[0][1] - 1, len(c))) )


