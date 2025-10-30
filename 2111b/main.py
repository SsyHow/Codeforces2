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
    n, m = MII()
    L = [1, 2]
    while len(L) < n +1:
        L.append(L[-1] + L[-2])
    ans = []
    for _ in range(m):
        x, y, z = sorted(MII())
        if L[-2] <= x and z >= L[-1]:
            ans.append(1)
        else:
            ans.append(0)
    print(*ans, sep = '')