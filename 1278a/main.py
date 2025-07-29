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
from collections import *
a = II()

for _ in range(a):
    s = I()
    t = I()
    if (n := len(s)) > (k := len(t)):
        print("NO")
        continue

    for i in range(k - n + 1):
        if Counter(s) == Counter(t[i:i + n]):
            print("YES")
            break
    else:
        print("NO")
