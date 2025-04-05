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

x, y = MII()
L1 = LII()
L2 = LII()
f = 0
for i in range(1, 10):

    if i in L1 and i in L2:
        f = i
        break

if f:
    print(f)
else:
    print(min(min(L1) * 10 + min(L2), min(L2) * 10 + min(L1)))