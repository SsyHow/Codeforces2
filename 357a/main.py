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

from itertools import accumulate
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = II()
L = LII()
x, y = MII()

L = list(accumulate(L))
for i in range(n):
    if x <= L[i] <= y and x <= L[-1] - L[i] <= y:
        print(i + 2)
        break
else:
    print(0)
