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
n, _ = MII()
L = LII()
ans = (0, 1, 0)
for idx, i in enumerate(L):
    if n // i * i > ans[0]:
        ans = (n // i * i, idx + 1, n // i)
print(ans[1], ans[2])