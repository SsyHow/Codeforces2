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
def add(x):
    k = 0
    for i in range(x):
        k ^= i
    return k
a = II()
for _ in range(a):
    x, y = MII()

    k = (0, x- 1, 1, x)[x % 4]
    print(x + (y != k) + (y ^ k == x))