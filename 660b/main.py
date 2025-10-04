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
n, m = MII()
L = []
k = n * 2
if m > n * 2:
    for i in range(1, n * 2 + 1):
        if i + k <= m:
            L.append(i + k)
        L.append(i)
    print(*L)
else:
    print(*range(1, m + 1))
