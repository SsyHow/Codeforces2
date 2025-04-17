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
from collections import Counter

a = II()
L = LII()
c = Counter(L)

k = c[5] // 9 * 9
if c[0] == 0:
    print(-1)
else:
    print('5' * k + '0' * c[0] if k > 1 else 0)