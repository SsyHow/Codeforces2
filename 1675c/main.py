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
    s = I()
    n = len(s)
    r0 = n - 1
    for i in range(n):
        if s[i] == '0':
            r0 = i
            break

    l1 = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            l1 = i
            break

    print(r0 - l1 + 1)