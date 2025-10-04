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
L = LII()
L1 = [0]
for i in L:
    L1.append(L1[-1] + i)
M = sorted(L)
M1 = [0]
for i in M:
    M1.append(M1[-1] + i)
b = II()
for _ in range(b):
    t, l, r = MII()
    if t == 2:
        print(M1[r] - M1[l - 1])
    else:
        print(L1[r] - L1[l - 1])

