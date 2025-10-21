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
from bisect import bisect_right
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    b = II()
    S = LII()
    L = sorted(S)
    vis = [True] * b
    tmp = 0
    M = []
    dic = {}
    for i in range(b - 1):
        xx = i
        if vis[i]:
            while i < b - 1 and L[i] + tmp >= L[i + 1]:
                vis[i + 1] = False
                tmp += L[i]
                i += 1
            tmp += L[i]
        M.append(tmp)

        dic[L[xx]] = M[xx]
    M.append(tmp + L[-1] if vis[-1] else tmp)
    dic[L[-1]] = M[-1]

    # print(M)
    # dic = {}
    # dic[L[0]] = M[0]
    # M = [L[0]]
    # for i in range(1, b):
    #     M.append(max(M[i - 1] + L[i], L[i]))
    #     dic[L[i]] = M[i]
    K = []
    # print(dic)
    for i in range(b):
        # print(L, S[i])
        K.append(bisect_right(L, dic[S[i]]) - 1)
    print(*K)