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
s = list(I())
n = len(s)
r = b = y = g = 0

dic = {}
for i in range(n):
    if s[i] != '!':
        dic[i%4] = s[i]

for i in range(n):
    if s[i] == '!':
        if dic[i % 4] == 'G':
            g += 1
        if dic[i % 4] == 'R':
            r += 1
        if dic[i % 4] == 'Y':
            y += 1
        if dic[i % 4] == 'B':
            b += 1
print(r, b, y, g)


