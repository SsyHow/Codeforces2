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
    b, c = MII()

    L = LII()
    ans = 0
    for i in range(c - 1):
        ans = max(ans, (L[i + 1] - L[i]) // 2 + 1)
    # print(ans + 1)
    ans = max(ans, L[0], b - L[-1]+ 1)
    print(ans)