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
    n, k = MII()
    L = []


    for _ in range(n):
        L.append(LII())
    ans = 0
    if n == 1:
        print("YES")
        continue
    for i in range(n // 2):
        for j in range(n):
            # print(i, j, n - i, n - j)
            if L[i][j] != L[n - i - 1][n - j - 1]:
                ans += 1

    if n & 1 == 1:
        for j in range(n // 2):
            if L[n // 2][j] != L[n // 2][n - j - 1]:
                ans += 1

    if n & 1 == 1 and k >= ans:
        print("YES")
    elif k >= ans and (k - ans) % 2 == 0:
        print("YES")
    else:
        print("NO")


