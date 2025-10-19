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

    used = [False] * (b + 1)

    L.sort(reverse=True)

    f = True

    for i in L:
        x = i
        while x > b or used[x]:
            x //= 2
        if x > 0:
            used[x] = True

        else:
            f = False
    print("YES" if f else "NO")