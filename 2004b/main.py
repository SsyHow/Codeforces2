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
    m, n = MII()

    if x > n or m > y:
        print(1)
        continue

    ll, rr = max(x, m), min(y, n)
    xl, xr = min(x, m), max(y, n)

    ans = rr - ll
    if xl < ll :
        ans += 1
    if xr > rr:
        ans += 1

    print(ans)
