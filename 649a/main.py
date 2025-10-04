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

def check(x):
    return (x & -x).bit_length() - 1

from collections import defaultdict
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
L = LII()
ans = 0
d = defaultdict(int)
for i in L:
    k = check(i)
    d[k] += 1
    ans = max(ans, k)
print(2 ** ans, d[ans])

