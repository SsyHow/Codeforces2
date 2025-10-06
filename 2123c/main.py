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
    b = II()
    L = LII()

    M = [0] * b
    M[0] = 1
    M[-1] = 1
    prev = L[0]
    next = L[-1]

    for i in range(b):
        if L[i] < prev:
            prev = L[i]
            M[i] = 1

    for i in range(b - 1, -1, -1):
        if L[i] > next:
            next = L[i]
            M[i] = 1
    print(*M, sep = '')
