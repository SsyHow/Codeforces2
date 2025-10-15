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
    L.sort()
    f = False

    e = o = 0
    if L[0] & 1 == 0:
        e += 1
    else:
        o += 1
    for i in range(1, b):
        if L[i] & 1 == 0:
            e += 1
        else:
            o += 1

        if not f and L[i] - L[i -1] == 1:
            f = True

    if e & 1 == o & 1 == 1 and f:
        print("YES")
    elif e & 1 == o & 1 == 0:
        print("YES")
    else:
        print("NO")
