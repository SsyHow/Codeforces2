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
    M = []
    vis = set()
    solo = set()
    for i in L:
        if i not in vis:
            vis.add(i)
            M.append(1)
        elif not solo:
            solo.add(i)
            M.append(2)
        elif i not in solo:
            M.append(3)
        else:
            M.append(1)
    if 3 in M:
        print(*M)
    else:
        print(-1)