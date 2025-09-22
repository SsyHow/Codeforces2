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
n, q = MII()
L = LII()
L.sort()
M = [0] * (n + 1)
for _ in range(q):
    x, y = MII()
    M[x - 1] += 1
    M[y] -= 1
for i in range(1,n+1):
    M[i] += M[i-1]


ans = 0
for x, y in zip(L, sorted(M[:-1])):
    ans += x * y
print(ans)

