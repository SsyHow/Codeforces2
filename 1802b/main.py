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
def check(k):

    if k <= 2:
        return k

    return k // 2 + 1

for _ in range(a):
    b = II()
    L = LII()

    cnt = 0
    tmp = 0
    n = 0
    for i in L:
        if i == 1:
            cnt += 1
            n += 1
        else:
            n = check(cnt)
        tmp = max(tmp, n)
    print(tmp)