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
    n = II()
    s = I()
    cnt = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            cnt += 1
    if cnt == 0:
        print(n + int(s[0] == '1'))
    elif cnt == 1:
        print(n + 1)
    else:
        print(n + cnt - 1 - (int(s[0] == '0' and cnt > 2)))

