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
from collections import defaultdict
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    s = I()
    t = I()
    p = I()

    c = defaultdict(int)
    for i in p:
        c[i] += 1

    p1 = 0
    k = len(s)
    d = defaultdict(int)
    for i in t:
        if p1 < k and s[p1] == i:
            p1 += 1
        else:
            d[i] += 1
            if d[i] > c[i]:
                print("NO")
                break
    else:
        print("YES" if p1 == k else "NO")