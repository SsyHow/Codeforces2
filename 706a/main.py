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
k = II()
tmp = float('inf')
for _ in range(k):
    x, y, v = MII()
    tmp = min(tmp, ((x - a) ** 2 + (y - b) ** 2) ** 0.5 / v)
print(tmp)