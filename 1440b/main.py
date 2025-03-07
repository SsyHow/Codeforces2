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
    n, k = MII()
    L = LII()

    x = n // 2
    ans = 0
    tmpk = 0

    while L:
        tmp = x
        while tmp:
            L.pop()
            tmp -=1
        ans += L.pop()
        tmpk += 1
        if tmpk == k:
            break
    print(ans)
