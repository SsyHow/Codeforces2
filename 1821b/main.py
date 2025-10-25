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
    L1 = LII()
    L2 = LII()

    l, r = 0, b - 1

    while l < r and L1[l] == L2[l]:
        l += 1
    while l < r and L2[r] == L1[r]:
        r -= 1


    while l > 0 and L2[l] >= L2[l - 1]:
        l -= 1
    while r < b - 1 and L2[r] <= L2[r + 1]:
        r += 1

    print(l + 1, r + 1)