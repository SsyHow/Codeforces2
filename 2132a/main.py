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
    b = II()
    s = I()
    c = II()
    s1 = I()
    s2 = I()

    k = []
    t = []

    for i in range(c):
        if s2[i] == 'D':
            t.append(s1[i])
        else:
            k.append(s1[i])

    print(''.join(k)[::-1] + s + ''.join(t))