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
L = []
for _ in range(k):
    b, c = MII()
    L.append((b, c))
L = sorted(L, key = lambda x: x[1], reverse = True)
# print(L)
ans = 0
for i in L:
    ans += min(i[0], n) * i[1]
    n -= i[0]
    if n <= 0:
        break
print(ans)

