import sys

input = sys.stdin.readline


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
    _ = I()
    k, n, m = MII()
    L1 = LII()
    L2 = LII()

    p = q = 0
    ans = []
    while p < n or q < m:
        if p < n and L1[p] <= k:
            ans.append(L1[p])
            if L1[p] == 0:
                k += 1
            p += 1
            continue
        if q < m and L2[q] <= k:
            ans.append(L2[q])
            if L2[q] == 0:
                k += 1
            q += 1
            continue
        print(-1)

        break
    else:

        print(*ans)