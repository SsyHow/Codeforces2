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
L = [0] * (a + 1)
for _ in range(a - 1):
    x, y = MII()
    L[x] += 1
    L[y] += 1
ans = 0
for idx, i in enumerate(L):
    if i == 1:
        ans += 1
print(ans)