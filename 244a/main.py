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
n, k = MII()
L = LII()
dic = defaultdict(set)
p0 = 0
vis = set()
for i in range(k):
    dic[i].add(L[p0])

    vis.add(L[p0])
    p0 += 1
for i in L:
    vis.add(i)
q = 1
# print(vis)
for i in dic:
    while len(dic[i]) < n:
        while q in vis:
            q += 1
        dic[i].add(q)
        vis.add(q)
for i in dic:
    print(*dic[i])
