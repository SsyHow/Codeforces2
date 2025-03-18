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
    n, a, b = MII()
    L = [0] * (n + 1)
    L[a] = L[b] = 1
    l = 1
    r = n
    X = [a]
    Y = [b]
    while len(X) < n // 2:
        while L[r] == 1:
            r -= 1
        X.append(r)
        L[r] = 1
    while len(Y) < n // 2 :
        while L[l] == 1:
            l += 1
        Y.append(l)
        L[l] = 1

    if min(X) == a and max(Y) == b:
        print(*X, *Y)
    else:
        print(-1)