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
L = LII()
ori = max([L[i] - L[i-1] for i in range(1, a)])

ans = float('inf')
for i in range(1, a-1):
    X = L[:i] + L[i + 1:]
    ori = max([X[i] - X[i-1] for i in range(1, a-1)])
    ans = min(ori, ans)
print(ans)