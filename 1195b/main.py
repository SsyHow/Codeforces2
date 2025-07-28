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
n, k = MII()
l, r = 0, n
while l <= r:
    mid = (l + r) // 2
    if mid * (mid + 3) == 2 * (k + n):
        print(n - mid)
        break
    elif mid * (mid + 3) > 2 * (k + n):
        r = mid - 1
    else:
        l = mid + 1


