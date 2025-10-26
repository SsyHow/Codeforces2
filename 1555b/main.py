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
    W, H = MII()
    x1, y1, x2, y2 = MII()
    x, y = MII()
    m = n = 1<< 60
    if W + x1 - x2 >= x:
        d = max(x1, W - x2)
        m = 0 if d >= x else x - d
    # print(m)
    if H + y1 - y2 >= y:
        d = max(y1, H - y2)
        n = 0 if d >= y else y - d
    # print(n)
    if m == n == 1 << 60:
        print(-1)
    else:
        print(min(m, n))