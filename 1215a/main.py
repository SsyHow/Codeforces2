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
a1 = II()
a2 = II()
k1 = II()
k2 = II()
n = II()
copyn = n
if k1 > k2:
    a1, a2 = a2, a1
    k1, k2 = k2, k1

p = min(n // k1, a1)
copyn -= p * k1
q = min(copyn// k2, a2)
# print(n, (k1 - 1) * a1 + (k2 - 1) * a2)
print(max((n - ((k1 - 1) * a1 + (k2 - 1) * a2)), 0), p + q)
