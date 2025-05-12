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



t = II()
for _ in range(t):
    n, m, sx, sy, d = MII()


    def check(i, j):
        return True if abs(sx - i) + abs(sy - j) <= d else False
    f = True
    if any(check(1, j) for j in range(1, m + 1)) or any(check(i, m) for i in range(1, n + 1)):
        f = False
    g = True
    if any(check(i, 1) for i in range(1, n + 1)) or any(check(n, j) for j in range(1, m + 1)):
        g = False

    print(n + m - 2 if g or f else -1)


