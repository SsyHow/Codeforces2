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
    b, k = MII()
    m, n = 0, 0
    for _ in range(b):
        x, y = MII()
        if x == k:
            m = 1
        if y == k:
            n = 1

    print("YES" if (m, n) == (1, 1) else "NO")