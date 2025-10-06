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


k = (a + 1) // 2 if a & 1 == 0 else a // 2

if b == a + 1:
    print(k)
elif b < a + 1:
    print((b - 1) // 2)
elif b > a * 2 + 1:
    print(0)
else:
    print((2 * a - b + 1) // 2)
