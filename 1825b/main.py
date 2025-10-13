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
t = II()
for _ in range(t):
    a, b = MII()
    L = LII()

    L.sort()
    if a < b:
        a, b = b, a
    print(max((L[-1] - L[0]) * (a - 1) * b + (L[-2] - L[0]) * (b - 1), (L[-1] - L[0]) * (a - 1) * b + (L[-1] - L[1]) * (b - 1)))