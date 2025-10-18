import sys

input = sys.stdin.readline


def I():
    return input().strip()


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
    b, c = MII()
    s = I()
    z = o = 0

    for i in s:
        if i == '1':
            z += 1
        else:
            o += 1
    mn = max(z, o) - b // 2
    mx = z // 2 + o // 2

    if mn <= c <= mx and (c - mn) & 1 == 0:
        print("YES")
    else:
        print("NO")

