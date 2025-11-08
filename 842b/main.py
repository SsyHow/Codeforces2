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
r, d = MII()

n = II()
ans = 0
for _ in range(n):
    x, y, ri = MII()

    k = (x * x + y * y) ** 0.5
    if k - ri >= r - d and k + ri <= r:
        ans += 1

print(ans)