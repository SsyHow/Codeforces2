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
    _ = I()
    n, k = MII()
    L1 = LII()
    L2 = LII()

    c = [float('inf')] * n
    for i in range(k):
        c[L1[i]-1] = L2[i]

    p = float('inf')
    L = [float] * n
    for i in range(n):
        p = min(c[i], p + 1)
        L[i] = p
    R = [0] * n
    for i in range(n - 1, -1, -1):
        p = min(c[i], p + 1)
        R[i] = p
    ans = []
    for i in range(n):
        ans.append(min(L[i], R[i]))
    print(*ans)