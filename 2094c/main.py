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
def b(L):
    c = 0
    for i in L:
        c ^= i
    return c
t = II()
for _ in range(t):
    n = II()

    x = b(range(1, 2 * n + 1))

    M = [0]
    for i in range(n):
        L = LII()
        if i == 0:
            for j in range(n):
                M.append(L[j])
                x ^= L[j]
        else:
            M.append(L[-1])
            x ^= L[j]
    M[0] = x
    print(*M)
