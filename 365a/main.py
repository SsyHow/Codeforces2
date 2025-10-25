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
a, x = MII()
ans = 0
for _ in range(a):
    b = II()
    vis = [False] * (x + 1)
    while b:
        if b % 10 <= x:
            vis[b % 10] = True
        b //= 10
    if all(i for i in vis):
        ans += 1
print(ans)
