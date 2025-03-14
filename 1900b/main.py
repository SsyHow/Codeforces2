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
    x, y, z = MII()
    L = []
    L.append(1 if y + z & 1 == 0 else 0)
    L.append(1 if x + z & 1 == 0 else 0)
    L.append(1 if y + x & 1 == 0 else 0)

    print(*L)