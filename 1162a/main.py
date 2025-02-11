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

n, h, m = MII()
L = [h] * n
for _ in range(m):
    l, r, x = MII()
    for i in range(l-1, r):
        L[i] = min(L[i], x)

print(sum([i *i  for i in L]))