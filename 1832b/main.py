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
    n, k = MII()
    L = LII()
    L.sort()

    M = [0]
    t = 0
    for i in L:
        t += i
        M.append(t)
    # print(M)
    ans = 0
    for i in range(k + 1):
        ans = max(ans, M[n - k + i] - M[2 * i])
    print(ans)