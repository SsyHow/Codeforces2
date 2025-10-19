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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    n, m = MII()
    L = LII()
    M = LII()

    L.sort()
    M.sort(reverse=True)

    ans = sum(abs(L[i] - M[i]) for i in range(n))
    for i in range(n-1, -1, -1):
        ans = max(ans, ans - abs(L[i] - M[i]) + abs(L[i] - M[m - n + i]) )
    print(ans)