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
    a, b, c, r = MII()
    a, b = sorted([a, b])
    x, y = c - r, c + r

    if r == 0 or a > y or b < x:
        print(b - a)
        continue

    ans = 0

    if a < x:
        ans += x - a

    if b > y:
        ans += b - y

    print(ans)