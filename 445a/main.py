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
a, b = MII()
L = []
for _ in range(a):
    L.append(list(I()))

for i in range(a):
    for j in range(b):
        if L[i][j] == '.':
            if (i + j) & 1 == 1:
                L[i][j] = 'W'
            else:
                L[i][j] = 'B'
for i in L:
    print(*i, sep = '')