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

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from collections import Counter
for _ in range(II()):
    n, k = MII()
    c = Counter(I())
    ans = 0
    for i in alpha:
        a = c[i]
        b = c[i.upper()]
        ans += min(a, b)
        # if abs(a - b) > 0:
        ans += min(k, abs(a - b)//2)
        k = max(0, k - abs(a - b)//2)
    print(ans)