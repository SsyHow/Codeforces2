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
M = [0] * a
vis = set()

L = LII()
for i in range(a - 1, -1, -1):
    vis.add(L[i])
    M[i] = len(vis)
for _ in range(b):
    print(M[II() - 1])