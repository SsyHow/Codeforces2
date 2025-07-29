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
b = II()
L = LII()
heapq.heapify(L)
cnt = 0
for i in range(1, b + 1):
    while L and L[0] < i:
        heapq.heappop(L)
    if not L:
        break
    heapq.heappop(L)
    cnt += 1
print(cnt)