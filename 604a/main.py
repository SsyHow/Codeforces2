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
L1 = LII()
L2 = LII()
ans = 0
hs, hu = MII()
for i in range(5):
    x = (i + 1) * 500
    ans += max(3 * x // 10, x - x // 250 * L1[i] - 50 * L2[i])

ans += hs* 100 - hu * 50
print(ans)