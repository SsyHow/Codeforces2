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
L = LII()

ans = -1
l = r = 0

while l < n:
    while r < n and L[r] - L[l] <= k:
        r += 1

    if r - l >= 3:
        ans = max(ans, (L[r - 1] - L[l + 1]) / (L[r - 1] - L[l])   )
    l += 1
print(ans)