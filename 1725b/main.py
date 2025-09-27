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
n, d = MII()
L = sorted(MII())
ans = 0
while L and L[-1] > d:
    ans += 1
    L.pop()

l, r = 0, len(L) - 1
while l < r:

    k = d // L[r] + 1
    if k + l - 1 <= r:
        ans += 1
        l += k - 1
        r -= 1
    else:
        break
print(ans)