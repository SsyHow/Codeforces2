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
    M = LII()
    k = M[-1]
    x = float('inf')
    ans = 1
    f = False
    for i in range(b):
        ans += abs(L[i] - M[i])
        x = min(x, min(abs(k - L[i]), abs(k - M[i])))
        if not f and (L[i] <= k <= M[i] or L[i] >= k >= M[i]):
            f = True

    ans += 0 if f else x
    print(ans)