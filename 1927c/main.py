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
    n, m, k = MII()

    L1 = LII()
    L2 = LII()

    p1 = p2 = p3 = 0
    cnt = [0]* (k + 1)
    for e in L1:
        if e <= k:
            cnt[e] |= 1
    for e in L2:
        if e <= k:
            cnt[e] |= 2

    c = [0] * 4

    for e in cnt:
        c[e] += 1


    if c[1] > k//2 or c[2] > k // 2 or c[1] + c[2] + c[3] < k:
        print("NO")
    else:
        print("YES")
