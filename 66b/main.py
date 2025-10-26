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
L = LII()
ans = 0
for i in range(a):
    l = r = i
    while l > 0 and L[l - 1] <= L[l]:
        l -= 1
    while r < a - 1 and L[r] >= L[r + 1]:
        r += 1

    ans = max(ans, r - l + 1)
print(ans)