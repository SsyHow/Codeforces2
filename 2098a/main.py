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
from collections import Counter
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    s = I()
    t = [int(i) for i in s]
    c = Counter(t)

    ans = []

    for i in range(9, -1, -1):
        for j in range(10):
            if j >= i and c[j] > 0:
                ans.append(j)
                c[j] -= 1
                break

    print(*ans, sep = '')




