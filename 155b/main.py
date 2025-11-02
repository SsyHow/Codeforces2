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
t = II()
L = []
for _ in range(t):
    a, b = MII()
    heapq.heappush(L, (-b, -a))

k = 1
ans = 0
while k > 0 and L :
    b, a = heapq.heappop(L)
    k += -b
    ans += -a
    k -= 1
print(ans)