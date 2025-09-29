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
n, a, b = MII()
L = LII()

ans = 0

for i in range((n + 1)//2 ):
    if L[i] != 2 and L[n - 1 - i] != 2 and L[i] != L[n - i - 1]:
        ans = -1
        break
    elif L[i] != 2 and L[n - 1 - i] == 2:
        ans += a if L[i] == 0 else b
    elif L[i] == 2 and L[n - 1 - i] != 2:
        ans += a if L[n - i - 1] == 0 else b
    elif L[i] == 2 and L[n - 1 - i] == 2:
        ans += min(a, b) * 2 if i != n - 1 - i else min(a, b)
print(ans)
