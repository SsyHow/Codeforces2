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
for _ in range(II()):
    n, m = MII()
    L = []
    for i in range(n):
        if i % 4 == 0 or i % 4 == 3:
            L.append([1, 0, 0, 1] * (m // 4) + [1, 0] * (2 == m % 4))
        else:
            L.append([0, 1, 1, 0] * (m // 4) + [0, 1] * (2 == m % 4))
    for i in L:
        print(*i)