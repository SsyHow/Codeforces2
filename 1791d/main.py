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
for _ in range(a):
    b = II()
    s = I()
    ans = 0
    c = Counter(s)
    k = set()
    for i in s:
        c[i] -= 1
        if c[i] == 0:
            c.pop(i)

        k.add(i)
        ans = max(ans, len(c) + len(k))
    print(ans)