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
    s = I()
    k = 0
    x = []
    for i in s:
        if i == 'T':
            k += 1
        else:
            x.append(i)
    print('T' * k + ''.join(x))