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
    L1 = LII()
    c = II()
    L2 = LII()

    o1 = e1 = o2 = e2 = 0
    for i in L1:
        if i & 1 == 1:
            o1 += 1
        else:
            e1 += 1
    for i in L2:
        if i & 1 == 1:
            o2 += 1
        else:
            e2 += 1
    print(o1 * o2 + e1 * e2)