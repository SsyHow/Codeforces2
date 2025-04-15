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
    n, m = MII()
    L = []
    for _ in range(n):
        L.append(LII())

    for i in range(n):
        for j in range(m):
            tmp = []
            if i > 0:
                if L[i - 1][j] >= L[i][j]:
                    continue
                tmp.append(L[i - 1][j])

            if i < n - 1:
                if L[i + 1][j] >= L[i][j]:
                    continue
                tmp.append(L[i + 1][j])

            if j > 0:
                if L[i][j - 1] >= L[i][j]:
                    continue
                tmp.append(L[i][j - 1])

            if j < m - 1:
                if L[i][j + 1] >= L[i][j]:
                    continue
                tmp.append(L[i][j + 1])
            if tmp:
                L[i][j] = max(tmp)
            # L[i][j] = max(tmp, default=L[i][j])

    for i in range(n):
        print(*L[i])