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

    x = []
    k = [x for x in L if x & 1]
    y = max(k) if k else 0
    ans = 0
    for i in L:
        if i & 1 == 0:
            heapq.heappush(x, i)
        else:
            y = max(i, y)

        while x and x[0] < y:
            ans += 1
            k = heapq.heappop(x)
            y += k
    # print(y, x)
    if y > 0 and x:
        ans += len(x) + 1
    print(ans)