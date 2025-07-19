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
t = II()
from collections import defaultdict
for _ in range(t):
    b = II()
    k = [0] * (b + 1)
    c = defaultdict(int)
    L = LII()

    for i in L:
        tmp = i
        while k[i] == 0:
            c[tmp] += 1
            k[i] = tmp
            i = L[i-1]
    # print(c)
    # print(k)
    for i in range(1, b + 1):
        print(c[k[i]], end = ' ')
    print()
