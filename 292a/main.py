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
q = 0
x = 0
ans = 0
pre = 0
for _ in range(a):
    t, c = MII()
    if q > 0:
        q -= min(q, t - pre)

    x = max(t, x)
    q += c
    ans = max(q, ans)
    pre = t
print(x + q, ans)
