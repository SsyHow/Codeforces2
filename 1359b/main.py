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
    n, m, x, y = MII()
    ans = 0
    for _ in range(n):
        s = I().split('*')
        for j in s:
            lj = len(j)
            ans += min(lj * x, (lj // 2) * y + (lj % 2) * x)
    print(ans)