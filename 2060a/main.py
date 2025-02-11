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
    a1, a2, a4, a5 = MII()
    L = []
    L.append(a1 + a2)
    L.append(a4 - a2)
    L.append(a5 - a4)

    count = 0
    for i in L:
        count = max(count, L.count(i))
    print(count)