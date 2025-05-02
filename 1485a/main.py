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
    x, y = MII()
    f = False
    if y == 1:
        f = True
        y += 1
    cnt = float('inf')
    for i in range(y, y + 11):
        ans = i - y
        tmp = x
        while tmp > 0:
            ans += 1
            tmp //= i
        cnt = min(ans, cnt)

    print(cnt + 1 if f else cnt)
