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
from random import getrandbits
RD = getrandbits(31)
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    n, k = MII()
    S = LII()
    T = LII()

    cnt = defaultdict(int)

    for x in S:
        r = x % k
        cnt[min(r, k - r) ^ RD] += 1

    for x in T:
        r = x % k
        cnt[min(r, k - r) ^ RD] -= 1
    # print(cnt)
    print("YES" if all(v == 0 for v in cnt.values()) else "NO")
