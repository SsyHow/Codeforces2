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
for _ in range(t):
    n, m = MII()
    if n > m:
        print("NO")
    elif n & 1 == 1:
        print("YES")
        print("1 " * (n -1), m - n + 1)
    elif n & 1 == m & 1 == 0:
        print("YES")
        print("1 " * (n - 2), (str((m - n + 2)// 2) + ' ') * 2)
    else:
        print("NO")