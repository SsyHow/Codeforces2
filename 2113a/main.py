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
t = II()
for _ in range(t):
    k, a, b, x, y = MII()

    if x > y:
        a, b = b, a
        x, y = y, x
    ans = 0
    if k >= a:
        ans += (k - a) // x + 1
        k -= (k - a) // x * x + x
    if k >= b:
        ans += (k - b) // y + 1
    print(ans)