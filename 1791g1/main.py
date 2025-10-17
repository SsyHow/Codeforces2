import sys

input = sys.stdin.readline


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

import heapq
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for _ in range(II()):
    n, c = MII()
    L = LII()
    M = []
    for idx, i in enumerate(L):
        heapq.heappush(M, i + idx + 1)
    ans = 0
    while M and c >= M[0]:
        c -= heapq.heappop(M)
        ans += 1
    print(ans)
