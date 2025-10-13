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
    a, b, x, y, n = MII()

    if (a - x) + (b - y) < n:
        print(x * y)

    else:
        t = min(a - x, n)
        p = min(b - y, n - t)

        t2 = min(b - y, n)
        p2 = min(a - x, n - t2)

        print(min((a - t) * (b - p), (b - t2) * (a - p2)))