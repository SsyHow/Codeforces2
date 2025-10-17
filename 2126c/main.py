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
    n, k = MII()
    L = LII()

    cur = L[k - 1]
    dis = L[k - 1]
    L.sort()
    ans = True
    for i in range(n):
        if L[i] < cur:
            continue
        if L[i] - cur > dis:
            ans = False

        cur = L[i]
    print("YES" if ans else "NO")