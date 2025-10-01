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
n, k = MII()
L = []
tmp = float("inf")
for _ in range(n):
    L.append( sorted(LII()))
for i in range(0, 1001):
    for x, y in L:
        if i < x or i > y:
            break

    else:
        tmp = min(tmp, abs(k - i))
else:
    print(tmp if tmp != float('inf') else -1)

