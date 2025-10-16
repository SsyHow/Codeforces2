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
    a, b, x, y = MII()
    if b < a:
        if b == a ^ 1:
            print(y)
        else:
            print(-1)
        continue

    ans = 0
    for i in range(a, b):
        if i ^ 1 == i + 1:
            ans += min(x, y)
        else:
            ans += x
    print(ans)
