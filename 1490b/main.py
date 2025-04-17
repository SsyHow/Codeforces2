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
    c = [0] * 3
    L = LII()
    for i in L:
        c[i % 3] += 1

    k = b // 3
    cnt = 0
    while any(c[i] != k for i in range(3)):
        for i in range(3):
            if c[i] > k:
                c[i] -= 1
                c[(i + 1) % 3] += 1
                cnt += 1
    print(cnt)