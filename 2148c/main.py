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
    n, m = MII()
    pa, pb = 0, 0
    ans = 0
    for _ in range(n):
        a, b = MII()
        tmp = 0
        if b != pb:
            tmp += (a - pa) - 1 if a & 1 == pa & 1 else (a - pa)
        else:
            tmp += (a - pa) if a & 1 == pa & 1 else (a - pa) - 1


        pa = a
        pb = b
        ans += tmp
    ans += (m - pa)
    print(ans)
