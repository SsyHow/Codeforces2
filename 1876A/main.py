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

t = II()
for _ in range(t):
    n, p = MII()
    L = LII()
    M = LII()

    K = list(zip(M, L))
    heapq.heapify(K)
    heapq.heappush(K, (p, 10 ** 5))
    n -= 1
    ans = 0
    while n > 0:
        a = (heapq.heappop(K))
        k = min(n, a[1])
        ans += k * a[0]
        n -= k
    print(ans + p)