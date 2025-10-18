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
    b = II()
    L1 = LII()
    L2 = LII()

    p = g = 0
    for i in range(b):
        if L1[i] > L2[i]:
            p += L1[i] - L2[i]
        # else:
        #     g += L2[i] - L1[i]
    print(p + 1)