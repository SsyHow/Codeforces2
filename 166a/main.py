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
n, k = MII()
dic = defaultdict(int)

for i in range(n):
    x, y = MII()
    dic[(x, y)] += 1

L = sorted(dic, key=lambda x: (-x[0], x[1]))

ans = 0
for i in L:
    ans += dic[i]
    if ans >= k:
        print(dic[i])
        break