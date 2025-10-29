import sys

input = lambda: sys.stdin.readline().rstrip()


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
L =  []
for _ in range(4):
    L.append(list(I()))

ok = False
for i in range(3):
    for j in range(3):
        x, y = 0, 0
        if L[i][j] == '#':
            x += 1
        else:
            y += 1
        if L[i + 1][j] == '#':
            x += 1
        else:
            y += 1
        if L[i][j + 1] == '#':
            x += 1
        else:
            y += 1
        if L[i + 1][j + 1] == '#':
            x += 1
        else:
            y += 1

        if x >= 3 or y >= 3:
            ok = True
    if ok:
        print("YES")
        break
else:
    print("NO")