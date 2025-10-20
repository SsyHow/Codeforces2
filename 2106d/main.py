import sys

input = lambda: sys.stdin.readline().rstrip()


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

def f(n, m, L1, L2):
    suf = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1]
        if L1[i] >= L2[m - 1 - suf[i]]:
            suf[i] += 1

            if suf[i] == m :
                return 0
    ans = 1 << 60
    if suf[0] == m -1:
        ans = L2[0]

    pre = 0
    for i, v in enumerate(L1):
        if v >= L2[pre]:
            pre += 1

        if pre + suf[i + 1] >= m:
            return 0

        if pre + suf[i + 1] == m - 1:
            ans = min(ans, L2[pre])

    if ans == 1 << 60:
        ans = -1
    return ans

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    n, m = MII()

    L1 = LII()
    L2 = LII()

    print(f(n, m, L1, L2))
