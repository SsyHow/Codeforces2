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
    ans = 1 << 60
    l = 0
    while l < b:
        r = l
        while r < b and L[r] == L[l]:
            r += 1


        r -= 1

        ans = min(ans, (l * L[l] + (b - r - 1) * L[l]))
        l = r + 1
    print(ans)
