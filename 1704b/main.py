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
    n, x = MII()
    cnt = 0
    L = LII()
    l, r = 0, float('inf')

    for i in L:
        l = max(l, i - x)
        r = min(r, i + x)

        if l > r:
            cnt += 1
            l, r = i - x, i + x
    print(cnt)