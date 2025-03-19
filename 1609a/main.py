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

a = II()
for _ in range(a):
    b = II()
    L = LII()
    k = 0
    for i in range(b):
        x = L[i]
        while x & 1 == 0:
            k += 1
            x >>= 1
        L[i] = x
    L.sort()
    print(L[-1] * (2 ** k) + sum(L[:-1]))
