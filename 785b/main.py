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
n = II()
x, y = 0, 1 << 60
for _ in range(n):
    a, b = MII()
    y = min(y, b)
    x = max(a, x)
m = II()
p, q = 0, 1 << 60
for _ in range(m):
    a, b = MII()
    q = min(q, b)
    p = max(p, a)
print(max(0, p - y, x - q))