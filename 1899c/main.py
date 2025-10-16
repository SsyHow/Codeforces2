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
    n = II()
    a = LII()

    ans = a[0]
    mn = min(0, a[0])
    sm = a[0]

    for i in range(1, n):
        if a[i] & 1 == a[i - 1] & 1:
            mn = 0
            sm = 0
        sm += a[i]
        ans = max(ans, sm - mn)
        mn = min(mn, sm)
    print(ans)