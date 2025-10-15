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
    n, d = MII()
    if n >= d:
        print("YES")
        continue

    l = 0
    r = n

    while l <= r:
        mid = (l + r) // 2
        if (n - mid) * (mid + 1) >= d:
            r = mid - 1
        else:
            l = mid + 1
    if l <= n:
        print("YES")
    else:
        print("NO")