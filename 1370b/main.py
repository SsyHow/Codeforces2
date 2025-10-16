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
    o = []
    e = []
    for i in range(b * 2):
        if L[i] & 1 == 1:
            o.append(i)
        else:
            e.append(i)

    if len(o) & 1 == 1:
        o.pop()
        e.pop()
    elif len(o) > 1:
        o.pop()
        o.pop()
    else:
        e.pop()
        e.pop()
    print()
    for i in range(0, len(o), 2):
        print(o[i] + 1, o[i + 1] +1)
    for i in range(0, len(e), 2):
        print(e[i] + 1, e[i + 1] + 1)