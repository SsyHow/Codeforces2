import sys

input = sys.stdin.readline


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
    b, c = MII()
    L = LII()
    M = LII()

    mx = []
    pre = []

    x = s = 0
    for i in range(b):
        x = max(x, M[i])
        mx.append(x)
        s += L[i]
        pre.append(s)

    ans = 0
    for j in range(min(b, c)):
        ans = max(ans, pre[j] + (c - j -1) * mx[j])
    print(ans)