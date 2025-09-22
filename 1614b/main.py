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
a = II()
for _ in range(a):
    b = II()
    L = LII()
    ans = [0] * (b + 1)

    k = []
    for i, x in enumerate(L, start=1):
        heapq.heappush(k, (-x, i))

    tmp = 1
    final = 0
    while k:
        x, y = heapq.heappop(k)
        ans[y] = tmp
        final += -x * abs(tmp) * 2
        if tmp < 0:
            tmp = -tmp + 1
        else:
            tmp = -tmp
    print(final)
    print(*ans)


