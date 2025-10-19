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
    L = [list(I()), list(I())]

    ans = 0
    for i in range(1, b - 1):
        if L[0][i] == 'x' or L[1][i] == 'x':
            continue

        if L[1][i - 1] == L[1][i + 1] == 'x' and L[0][i - 1] == L[0][i + 1] == '.':
            ans += 1

        if L[0][i - 1] == L[0][i + 1] == 'x'and L[1][i - 1] == L[1][i + 1] == '.':
            ans += 1
    print(ans)