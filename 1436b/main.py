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
    m = [[0 for _ in range(b)] for _ in range(b)]

    for i in range(b):
        m[i][i] = 1
        m[i][b - i - 1] = 1

    if b & 1 == 1:
        m[b //2 -1][b//2] =1
        m[b//2][b//2 +1] = 1
    for i in m:
        print(*i)