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

a, b, c, d = MII()

m = max(3 * a / 10, a - a//250 * c)
v = max(3 * b / 10, b - b//250 * d)

if v == m:
    print("Tie")
elif v > m:
    print("Vasya")
else:
    print("Misha")