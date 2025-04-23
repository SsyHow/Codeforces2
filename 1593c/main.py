
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
import heapq
a = II()
for _ in range(a):
    n, k = MII()
    L = LII()
    M = []
    for i in L:
        heapq.heappush(M, n - i)
    ans = 0
    heapq.heappush(M, float('inf'))
    while n > M[0] :
        n -= heapq.heappop(M)
        ans += 1
    print(ans)