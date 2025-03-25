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
    s = I()
    k = defaultdict(int)
    for i in s:
        k[i] += 1

    k = sorted(k.items(), key = lambda x: -x[1])
    s = s.replace(k[-1][0], k[0][0], 1)
    print(s)