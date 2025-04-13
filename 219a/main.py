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
s = I()

c = Counter(s)
L = []
for i in c:
    if c[i] % a != 0:
        print(-1)
        break
    L.append(c[i] // a * i)
else:
    print(''.join(L) * a)