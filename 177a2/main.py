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
L = []
for _ in range(a):
    L.append(LII())

ans = 0
for i in range(a):
    ans += L[i][i]
    ans += L[i][a - i - 1]

    ans += L[a//2][i]
    ans += L[i][a//2]

ans -= 3 * L[a//2][a//2]
print(ans)