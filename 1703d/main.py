import sys

input = sys.stdin.readline


def I():
    return input().strip()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):

    a = II()
    L = []
    vis = set()
    for _ in range(a):
        k = I()
        L.append(k)
        vis.add(k)
    M = [0] * a
    for idx, i in enumerate(L):
        for j in range(1, len(i)):
            # print(i[:j], i[j:])
            if i[:j] in vis and i[j:] in vis:
                M[idx] = 1
    print(*M, sep='')