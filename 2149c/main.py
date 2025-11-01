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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    n, k = MII()
    L = LII()

    cnt = [0] * k

    kk = 0
    for i in range(n):
        if L[i] == k:
            kk += 1
        if L[i] < k:
            cnt[L[i]] += 1

    ans = 0
    for i in range(k):
        if not cnt[i]:
            ans += 1
    print(max(ans, kk))