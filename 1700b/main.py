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
    L = I()
    ans = []
    for i in L:
        ans.append(9 - int(i))
    if L[0] == '9':
        M = [1] * b
        M[-1] += 1
        f = False
        for i in range(b - 1, -1, -1):
            if ans[i] + M[i] + f > 9:
                ans[i] += M[i] + f
                ans[i] %= 10
                f = True
            else:
                ans[i] += M[i] + f
                ans[i] %= 10
                f = False
    print(*ans, sep = '')

