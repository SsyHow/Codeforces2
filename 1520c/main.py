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
for i in range(a):
    b = II()
    if b == 2:
        print(-1)
        continue
    L = list(range(1, b ** 2 + 1, 2)) + list(range(2, b ** 2 + 1, 2))
    ans = [[0 for _ in range(b)] for _  in range(b)]

    for x in range(b):
        for y in range(b):
            ans[x][y] = L[x * b + y]
    for i in range(b):
        print(*ans[i])