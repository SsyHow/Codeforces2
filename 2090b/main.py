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
    L = []
    x, y = MII()
    for _ in range(x):
        L.append(list(map(int, I())))
    for i in range(x):
        k = 0
        while k < y and L[i][k] > 0:
            L[i][k] = 2
            k += 1

    for j in range(y):
        k = 0
        while k < x and L[k][j] > 0:
            L[k][j] = 2
            k += 1

    if any(any(L[i][j] == 1 for j in range(y)) for i in range(x)):
        print("NO")
    else:
        print("YES")
