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
import heapq
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n, k = MII()
L = LII()
x1 = []
x2 = []
ans1 = ans2 = 0
for i in L:
    heapq.heappush(x1, i)
    heapq.heappush(x2, -i)

while n:
    tmp = heapq.heappop(x1)
    ans1 += tmp
    if tmp > 1:

        heapq.heappush(x1, tmp - 1)

    tmp = -heapq.heappop(x2)
    ans2+= tmp
    heapq.heappush(x2, -(tmp - 1))
    n -= 1
print(ans2, ans1)

