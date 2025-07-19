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
    n, k, b, s = MII()

    if k * b > s or s > k * b + (k - 1) * n:
        print(-1)
        continue

    L = [0] * n
    L[0] = k * b
    su = k * b
    for i in range(n):
        add = min(s - su, k - 1)
        L[i] += add
        su += add
    print(*L)
