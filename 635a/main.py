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
r, c, n, k = MII()
L = []
ans = 0
for _ in range(n):
    x, y = MII()
    L.append((x -1, y - 1))

for i0 in range(r):
    for j0 in range(c):
        for i1 in range(i0, r):
            for j1 in range(j0, c):
                tmp = 0
                for x, y in L:
                    if i0 <= x <= i1 and j0 <= y <= j1:
                        tmp += 1
                if tmp >= k:
                    ans += 1
print(ans)