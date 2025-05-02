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
from collections import defaultdict
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def build(L):
    prev = L[0]
    cnt = 0
    c = defaultdict(int)
    for i in L:
        if i == prev:
            cnt += 1
        else:
            c[prev] = max(c[prev], cnt)
            cnt = 1
            prev = i
    return c
a = II()
for _ in range(a):
    b = II()
    L1 = LII()
    L1.append(-1)
    L2 = LII()
    L2.append(-1)
    c1 = build(L1)
    c2 = build(L2)
    tmp = 0
    for i in set(c1.keys()).union(set(c2.keys())):
        tmp = max(tmp, c1[i] + c2[i])
    print(tmp)

