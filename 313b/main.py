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
s = I().strip()
L = [0]
for i in range(len(s)-1):
    L.append(L[-1] + 1 if s[i] == s[i + 1] else L[-1])
a = II()
# print(L)
for _ in range(a):
    x, y = MII()
    print(L[y-1] - L[x-1])