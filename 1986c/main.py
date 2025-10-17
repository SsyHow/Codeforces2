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
a = II()
for _ in range(a):
    n, m = MII()
    LL = list(I())
    L = LII()
    M = list(I())

    L = sorted(set(L))

    M.sort()
    # print(M, LL, L)
    for i in range(len(L)):
        # print(i)
        LL[L[i] - 1] = M[i]

    print(''.join(LL))
