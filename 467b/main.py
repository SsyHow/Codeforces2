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
n, m, k = MII()
L = []
for _ in range(m):
    L.append(II())
c = II()
ans = 0
for i in L:
    n = i ^ c
    count = 0
    while n:
        n = n & (n - 1)
        count += 1

    if count <= k:
        ans += 1
print(ans)