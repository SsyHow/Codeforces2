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
    w, h = MII()
    x0 = LII()
    xn = LII()
    y0 = LII()
    yn = LII()

    k1 = x0[-1] - x0[1]
    k2 = xn[-1] - xn[1]
    k3 = y0[-1] - y0[1]
    k4 = yn[-1] - yn[1]
    print(max(max(k1, k2) * h, max(k3, k4) * w))
