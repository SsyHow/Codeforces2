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
h = set()
v = set()
L = []
for i in range(a * a):
    x, y = MII()
    if x in h or y in v:
        continue
    else:
        L.append(i + 1)
        h.add(x)
        v.add(y)
print(*L)