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
t = II()
L = LII()
L.sort()
if L[-1] >= L[-2] + L[-3]:
    print("NO")
else:
    print("YES")
    for i in range(t - 1, -1, -2):
        print(L[i], end = ' ')
    for i in range(t % 2, t, 2):
        print(L[i], end = ' ')