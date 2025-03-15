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
from collections import defaultdict
a = II()
for _ in range(a):
    b = II()
    L = LII()
    ans = 0
    k = defaultdict(int)
    for i in range(b):
        ans += k[L[i].bit_length()]
        k[L[i].bit_length()] += 1

    print(ans)