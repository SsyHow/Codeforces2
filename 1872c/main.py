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

def f(n):
    L = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if L[i]:
            for j in range(i * i, n + 1, i):
                L[j] = False
    return L
def xx(x, y):
    for i in range(x, y + 1):
        # print(L[i])
        if not L[i]:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    return j, i - j
    return -1,
L = f(10 ** 7 + 1)
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    x, y = MII()
    print(*xx(x, y))


