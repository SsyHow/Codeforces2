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
    s = I()
    t = I()

    n = len(s)
    m = len(t)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i, x in enumerate(s):
        for j, y in enumerate(t):
            if x == y:
                dp[i + 1][j + 1] = dp[i][j] + 1

    print(n + m - 2 * max(map(max, dp)))