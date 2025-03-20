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
    n, m, k = MII()
    x, y = MII()
    ans = "YES"
    for _ in range(k):
        xx, yy = MII()
        if (x + y) & 1 == (xx + yy) & 1:
            ans = "NO"

    print(ans)