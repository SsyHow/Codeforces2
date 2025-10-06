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
a, b, c, d = MII()

if a == c:
    k = abs(b - d)
    x = m = k + a if k + a <= 1000 else a - k
    y = b
    n = d
    print(x, y, m, n)
elif b == d:
    k = abs(a - c)
    y = n = k + b if k + b <= 1000 else b - k
    x = a
    m = c
    print(x, y, m, n)
elif abs(c - a) == abs(d - b):
    x = a
    y = d
    m = c
    n = b
    print(x, y, m, n)
else:
    print(-1)