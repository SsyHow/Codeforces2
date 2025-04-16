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
    n, k, q = MII()
    L = LII()

    ans = x = 0

    for i in L:
        if i <= q:
            x += 1

        else:
            if x >= k:
                ans += (x - k + 1) * (x - k + 2) // 2
            x = 0
    if x >= k:
        ans += (x - k + 1) * (x - k + 2) // 2

    print(ans)
