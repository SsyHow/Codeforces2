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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
mod = 10 ** 9 + 7
for _ in range(a):
    n, k = MII()
    L = LII()

    curr = L[0]
    best = L[0]
    s = L[0]
    for i in L[1:]:
        curr = max(0, curr) + i
        best = max(best, curr)
        s += i
    best = max(0, best)
    print((best * (2 ** k - 1) + s) % mod)

