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
    n, q = MII()
    L = LII()
    M = LII()
    x = [0] * 31

    for j in M:
        x[j] += 1
        if x[j] == 1:
            for i in range(n):
                if L[i] % (2 ** j) == 0:
                    L[i] += 1 << (j - 1)
    print(*L)