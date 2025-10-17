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
from math import factorial
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
mod = 10 ** 9  + 7
for _ in range(a):
    b = II()
    L = LII()
    M = LII()

    L.sort(reverse=True)
    M.sort(reverse=True)
    i = j = 0
    ans = 1

    while i < len(L) and j < len(M):

        while i < len(L) and L[i] > M[j]:
            # print(L[i], L[j])
            i += 1
        # print(i, j)
        ans = ans * (i - j) % mod
        j += 1
    if i > j:
        for x in range(i - j, 0, -1):
            ans = ans * x %mod
    print(ans)

