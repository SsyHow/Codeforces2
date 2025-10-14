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
from math import gcd
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def check(L):
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            return False
    return True

for _ in range(II()):
    b = II()
    L = LII()
    k1 = k2 = 0
    for i in range(0, len(L), 2):
        k1 = gcd(k1, L[i])
    for i in range(1, len(L), 2):
        k2 = gcd(k2, L[i])
    # print(k1, k2)
    M1 = [i % k1 == 0 for i in L]
    M2 = [i % k2 == 0 for i in L]

    if check(M1):
        print(k1)
    elif check(M2):
        print(k2)
    else:
        print(0)