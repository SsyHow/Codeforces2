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
t = II()
for _ in range(t):
    a, b, c = MII()
    e, f, g = MII()

    m = min(a, g)
    a -= m
    g -= m

    m = min(b, e)
    b -= m
    e -= m

    m = min(c, f)
    c -= m
    f -= m
    ans = 2 * m

    ans -= 2 * min(b, g)

    print(ans)

