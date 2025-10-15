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
    b = II()
    L = LII()
    l = x = y = 0
    r = b
    ans = 0
    while l < r:
        x += L[l]
        l += 1
        while l < r and y < x:
            r -= 1
            y += L[r]


        if x == y:
            ans = (l + b - r)

    print(ans)