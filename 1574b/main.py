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
    x, y, z, m = MII()
    x, y, z = sorted((x, y, z))
    mx = x - 1 + y - 1 + z - 1
    mn = max(0, z - 1 - (x + y))
    if mn <= m <= mx:
        print("YES")
    else:
        print("NO")

