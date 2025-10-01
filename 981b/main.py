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
d = defaultdict(int)
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for _ in range(II()):
    x, y = MII()
    d[x] = max(d[x], y)

for _ in range(II()):
    x, y = MII()
    d[x] = max(d[x], y)
ans = 0
for i in d:
    ans += d[i]
print(ans)