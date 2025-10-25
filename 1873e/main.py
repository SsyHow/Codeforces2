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



def calc(h):
    ans = 0
    for i in L:
        ans += max(0, h - i)
    return ans
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    b, c = MII()
    L = LII()

    l, h = 0, 3 * 10 ** 9

    while l <= h:
        mid = (l + h) // 2
        if calc(mid) <= c:
            l = mid + 1
        else:
            h = mid - 1

    print(h)


