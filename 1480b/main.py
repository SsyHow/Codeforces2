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
    A, B, n = MII()
    L1 = LII()
    L2 = LII()

    L = sorted(zip(L1,L2), reverse=True)

    while B > 0:
        if not L:
            break
        a, b = L.pop()

        B -= (b + A - 1) // A * a
    # print(L, a, n)
    if not L and a + B > 0:
        print("YES")
    else:
        print("NO")