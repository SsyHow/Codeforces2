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
t = 'Bulbasaur'
tdic = defaultdict(int)
for i in t:
    tdic[i] += 1

k = I()
kdic = defaultdict(int)
for i in k:
    kdic[i] += 1

ans = float('inf')

for i in tdic:
    ans = min(ans, kdic[i] // tdic[i] )
print(ans)

