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
from math import lcm
a = II()
for _ in range(a):
    b = II()
    k = 1
    g = 2
    while g * g <= b:
        if b % g == 0:
            k = b // g
            break
        g += 1
    print(k, b - k)
