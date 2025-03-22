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
    L = []
    for i in range(b):
        s = list(I())
        s = list(map(int, s))
        L.append(s)
    x = y = 0
    x = sum([sum(L[i]) & 1 == 1 for i in range(b)])
    L = list(zip(*L))
    y = sum([sum(L[i]) & 1 == 1 for i in range(c)])
    print(max(x, y))