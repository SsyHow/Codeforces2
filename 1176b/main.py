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
a = II()
for _ in range(a):
    b = II()
    L = LII()
    ans = 0
    x1 = x2 = 0
    for i in L:
        if i % 3 == 0:
            ans += 1
        elif i % 3 == 1:
            x1 += 1
        else:
            x2 += 1

    k = min(x1, x2)
    ans += k
    ans += (x1 - k) // 3 + (x2 - k) // 3
    print(ans)