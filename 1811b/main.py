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
    n, x1, y1, x2, y2 = MII()
    n += 1
    c1 = min(n - x1, x1, n - y1, y1)
    c2 = min(n - x2, x2, n - y2, y2)

    print(abs(c1 - c2))