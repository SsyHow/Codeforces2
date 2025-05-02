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
n, k = MII()
L = LII()

ans = 0

for i in range(1, n):
    if L[i] + L[i - 1] < k:
        ans += k - L[i - 1] - L[i]
        L[i] = k - L[i - 1]

print(ans)
print(*L)