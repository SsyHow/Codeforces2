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
a = II()
for _ in range(a):
    b = II()
    L = LII()

    c12 = defaultdict(int)
    c13 = defaultdict(int)
    c23 = defaultdict(int)

    c3 = defaultdict(int)
    ans = 0
    for i in range(b - 2):
        x, y, z = L[i], L[i + 1], L[i + 2]
        ans += c12[(x, y)] + c13[(x, z)] + c23[(y, z)] - c3[(x, y, z)] * 3
        c12[(x, y)] += 1
        c13[(x, z)] += 1
        c23[(y, z)] += 1
        c3[(x, y, z)] += 1
    print(ans)
