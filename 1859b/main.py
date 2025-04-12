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
    x = []
    m = s = float('inf')
    k = 0
    for _ in range(b):
        c = II()
        x1, x2 = sorted(MII())[:2]

        m = min(m, x1)
        k += x2
        s = min(x2, s)
    print(m + k - s)