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

T = II()
for _ in range(T):
    n = II()
    L = LII()

    d = L[1] - L[0]
    for i in range(2, n):
        if L[i] - L[i - 1] != d:
            print("NO")

            break
    else:

        v = L[0] - d
        if d < 0:
            v = L[-1] + d

        if v >= 0 and v % (n + 1) == 0:
            print("YES")
        else:
            print("NO")

