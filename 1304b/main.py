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
v = set()
ans = 0
tmp = 0
x = ''
L = []
for _ in range(a):
    k = I()
    if k[::-1] in v:
        ans += 2
        L.append(k)
    elif k == k[::-1]:
        tmp = 1
        x = k
    else:
        v.add(k)
print((ans + tmp) * b)
xv = ''.join(L)
print(xv + x + xv[::-1])
