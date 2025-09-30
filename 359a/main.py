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
x, y = MII()
L = []
for _ in range(x):
    L.append(LII())

ans = 4
for i in range(x):

    for j in range(y):
        tmp = 0
        if L[i][j] == 1:
            if i > 0:
                tmp += 1
            if i < x - 1:
                tmp += 1
            if j > 0:
                tmp += 1
            if j < y - 1:
                tmp += 1
            if tmp == 3:
                ans = 2
print(ans)