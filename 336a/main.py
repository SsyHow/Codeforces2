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
k = (abs(a) + abs(b))
x = -k if a < 0 else k
y = -k if b < 0 else k
xx = (x, 0)
yy = (0, y)
xx, yy = sorted((xx, yy), key = lambda x: x[0])
print(*xx, *yy)