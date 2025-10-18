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
from bisect import bisect_left
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    b = II()
    L = LII()

    if L[0] != len(L):
        print("NO")
        continue

    k = []
    for i in range(b, 0, -1):
        while len(k) < L[i - 1]:
            k.append(i)
    for i in range(b):
        if k[i] != L[i]:
            print("NO")
            break
    else:
        print("YES")
    # print(k)
