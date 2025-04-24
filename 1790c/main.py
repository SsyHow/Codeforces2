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
    c = Counter()
    K = []
    f = True
    k = 0
    m = True
    for _ in range(b):
        L = LII()
        c[L[0]] += 1
        if c[L[0]] >= 2:
            k = L[0]
        if k:
            if not m:
                if L[0] != k:
                    print(k, *L)
            else:

                for i in K:
                    if i[0] != L[0] and f:
                        print(k, *i)
                        f = False
                        break
                else:
                    m = False



        K.append(L)


