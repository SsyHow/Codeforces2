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
x, y = MII()
k = 0
for _ in range(a-1):
    m, n = MII()
    k += ((m - x) * (m - x) + (n - y) * (n - y)) ** 0.5
    x, y  = m, n
print(k * b / 50)