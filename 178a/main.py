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
n = II()
a = LII()
ans = 0
for i in range(n-1):
    t = 0
    while i + 2 ** (t + 1) < n:
        t += 1
    a[i + 2 ** t] += a[i]
    ans += a[i]
    a[i] = 0
    print(ans)