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
s = I()
if len(s) & 1 == 1:
    print(-1)
else:
    x = y = 0
    for i in s:
        if i == 'U':
            x += 1
        elif i == 'D':
            x -= 1
        elif i == 'L':
            y += 1
        elif i == 'R':
            y -= 1
    print((abs(x) + abs(y)) // 2)
