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
a, b = MII()
L = LII()

m, n = MII()
M = LII()

cnt1 = cnt2 = 0
x = 0
for i in L:
    x = x * b + i
    # cnt1 += 1
y = 0
for i in M:
    y = y * n + i
    # cnt2 += 1
if x == y:
    print("=")
else:
    print(">" if x > y else "<")