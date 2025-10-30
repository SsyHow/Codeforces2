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
for _ in range(a):
    b = II()
    L = LII()
    ans = 0
    M = [0] * (b + 1)

    for i in range(0, b, 2):
        mn = L[i]
        if i >= 2:
            mn = min(mn, L[i - 1] - M[i - 2])
        if i + 1 < b:
            mn = min(mn, L[i + 1])
        M[i] = mn
        ans += L[i] - M[i]
    print(ans)