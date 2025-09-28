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
n, m, k = MII()
L = LII()
mx, smx = max(L[:2]), min(L[:2])

for i in L[2:]:
    if i > mx:
        smx = mx
        mx = i
    elif i > smx:
        smx = i
a, b = divmod(m, (k + 1))
print((a * k + b) * mx + a * smx)
