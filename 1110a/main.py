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
a, b = MII()
L = LII()
ans = 0

f = a & 1

for idx, i in enumerate(L):
    if b - idx - 1 == 0 and i & 1 == 1:
        ans += 1

    elif b - idx - 1 > 0 and i & 1 == 1 and f:
        ans += 1

print('odd' if ans & 1 == 1 else 'even')