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
    n, s = MII()
    L = LII()
    if s <= L[0]:
        print(L[-1] - s)
    elif s >= L[-1]:
        print(s - L[0])

    else:
        print(min((s - L[0]) * 2 + (L[-1] - s), (L[-1] - s) * 2 + (s - L[0])))