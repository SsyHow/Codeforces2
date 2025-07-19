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
    L = LII()

    k = -1
    for i in L:
        k &= i
    if k > 0:
        print(1)
        continue
    tmp = -1
    i = 0
    cnt = 0
    for i in L:
        tmp &= i
        if tmp == k:
            cnt += 1
            tmp = -1
    print(cnt)

