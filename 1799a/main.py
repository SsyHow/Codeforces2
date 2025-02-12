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
from collections import deque

a = II()
for _ in range(a):
    x, y = MII()
    L = LII()

    s = set()
    k = deque()
    tmp = ans = 0
    for i in L:
        s.add(i)
        ans += 1
        if len(s) > tmp:
            k.appendleft(ans)
            tmp += 1
        if len(k) == x:
            # print(*k)
            break
    # else:
    while len(k) < x:
        k.appendleft(-1)
    print(*k)




