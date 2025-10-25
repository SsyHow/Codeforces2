import sys

input = lambda: sys.stdin.readline().rstrip()


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
from bisect import bisect_left
L = []
k = 10 ** 10
i = 1
x = (i + 1) * i // 2 * 3 - i
while x <= k:
    L.append(x)
    i += 1
    x = (i + 1) * i // 2 * 3 - i

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    b = II()
    ans = 0
    while b >= 2:
        t = bisect_left(L, b)
        if b != L[t]:
            t -= 1
        b -= L[t]
        ans += 1
    print(ans)
