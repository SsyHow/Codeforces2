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
    x = L[0]
    y = L[-1]
    p0 = p2 = 0
    p1 = p3 = b - 1

    while p0 < b and L[p0] == x:
        p0 += 1

    while p0 < p1 and L[p1] == x:
        p1 -= 1

    while p2 < b and L[p2] == y:
        p2 += 1

    while p2 < p3 and L[p3] == y:
        p3 -= 1

    print(min(p1 - p0 + 1, p3 - p2 + 1))
