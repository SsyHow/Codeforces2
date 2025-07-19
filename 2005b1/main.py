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
    n, m, q = MII()
    L = sorted(LII())

    b = II()

    if b < L[0]:
        print(L[0] - 1)
    elif b > L[-1]:
        print(n - L[-1])
    else:
        for i in range(m - 1):
            if L[i] <= b <= L[i + 1]:
                print((L[i + 1] - L[i]) // 2)
