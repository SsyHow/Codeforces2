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
from collections import defaultdict
def g(L):
    M = []
    dic = defaultdict(int)
    for i in L:
        dic[i] += 1
    for i in L:
        M.append(dic[i])
    return M

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    b = II()
    L = LII()

    query = [L[:]]
    xx = g(L)
    while xx != query[-1]:
        query.append(xx)
        xx = g(query[-1])


    # print(query)
    n = II()
    nn = len(query)
    for _ in range(n):
        x, k = MII()
        if k < nn:
            print(query[k][x - 1])
        else:
            print(query[-1][x - 1])