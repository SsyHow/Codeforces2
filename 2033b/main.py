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
    b = II()
    L = []
    for _ in range(b):
        L.append(LII())
    k = defaultdict(int)

    for i in range(b):
        for j in range(b):
            if L[i][j] < 0:
                k[i-j] = max(k[i-j], -L[i][j])

    ans = 0
    for i in k:
        ans += k[i]

    print(ans)