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

n, p1, p2, p3, t1, t2 = MII()
start, end = MII()
ans = (end - start) * p1
for _ in range(n-1):
    x, y = MII()
    ans += (y - x) * p1

    k = x - end

    if k <= t1:
        ans += k * p1
    else:
        k -= t1
        ans += t1 * p1

        if k > t2:
            k -= t2
            ans += t2 * p2
            ans += k * p3
        else:
            ans += k * p2
    start, end = x, y
print(ans)
