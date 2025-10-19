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
t = I()
if len(s) != len(t):
    print("NO")
else:

    c = {}
    for i in range(len(s)):
        if s[i] != t[i]:
            c[i] = {s[i], t[i]}
    k = list(c.values())
    print("YES" if len(k) == 2 and k[0] == k[1] else "NO")