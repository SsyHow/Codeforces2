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
a, b = MII()
L = []
x = y = 0
for _ in range(a):
    m, n = MII()
    x += n
    y += m
    L.append([m, n])
if x > b:
    print(-1)
else:
    L.sort(key = lambda x: x[0] - x[1])
    ans = 0
    while L and y > b:
        m, n = L.pop()
        y -= m - n
        ans += 1
    print(ans)
