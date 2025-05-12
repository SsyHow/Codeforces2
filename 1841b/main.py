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

    f = True

    M = []
    prev = L[0]
    for i in L:
        if f and prev <= i:
            M.append(1)
            prev = i

        elif f and prev > i:
            if i <= L[0]:
                M.append(1)
                prev = i
                f = False
            else:
                M.append(0)

        elif not f and prev <= i and i <= L[0]:
            M.append(1)
            prev = i
        else:
            M.append(0)

    print(*M, sep='')
