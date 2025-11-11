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
n, m, k = MII()
L = [0] * (n * m)
for i in range(k):
    x, y = MII()
    x -= 1
    y -= 1
    L[x * m + y] = 1
    if x > 0 and y > 0 and L[(x - 1) * m + (y - 1)] == 1 and L[x * m + (y - 1)] == 1 and L[(x - 1) * m + y] == 1:
        print(i + 1)
        break
    if x > 0 and y < m - 1 and L[(x - 1) * m + (y + 1)] == 1 and L[x * m + (y + 1)] == 1 and L[(x - 1) * m + y] == 1:
        print(i + 1)
        break
    if x < n - 1 and y > 0 and L[(x + 1) * m + (y - 1)] == 1 and L[x * m + (y - 1)] == 1 and L[(x + 1) * m + y] == 1:
        print(i + 1)
        break
    if x < n - 1 and y < m - 1 and L[(x + 1) * m + (y + 1)] == 1 and L[x * m + (y + 1)] == 1 and L[(x + 1) * m + y] == 1:
        print(i + 1)
        break
else:
    print(0)

