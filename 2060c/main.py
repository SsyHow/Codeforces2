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
    b, c = MII()
    L = LII()
    L.sort()

    p1, p2 = 0, b-1
    ans = 0
    while p1 < p2:
        s = L[p1] + L[p2]
        if s == c:
            p1 += 1
            p2 -= 1
            ans += 1
        elif s > c:
            p2 -= 1
        else:
            p1 += 1
    print(ans)