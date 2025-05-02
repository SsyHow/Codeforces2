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
    x = y = 1

    L = set()
    while b and x < c:
        L.add(x)
        x += y
        y += 1
        b -= 1
    k = c
    while b:
        while k in L:
            k -= 1
        b -= 1
        L.add(k)
    print(*sorted(L))
