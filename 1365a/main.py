import sys

input = sys.stdin.readline


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

a = II()
for _ in range(a):
    n, m = MII()
    row = [True] * n
    col = [True] * m
    L = []
    for _ in range(n):
        L.append(LI())
    for i in range(n):
        for j in range(m):
            if L[i][j] == '1':
                row[i] = False
                col[j] = False

    k = min(row.count(True), col.count(True))

    print("Ashish" if k & 1 else "Vivek")