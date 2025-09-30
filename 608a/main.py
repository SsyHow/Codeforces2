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
a, b = MII()
L = []
for _ in range(a):
    L.append(LII())

L.sort(reverse=True, key = lambda x: x[0])
ans = 0
curr = b

for x, y in L:
    ans += curr - x
    if y > ans:
        ans = y
    curr = x

ans += curr
print(ans)
