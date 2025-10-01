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
ans = 1
prev = L[0]
tmp = 1
for i in L[1:]:
    if i == prev:
        ans = max(ans, tmp)
        tmp = 1
    else:
        tmp += 1
    prev = i

ans = max(ans, tmp)
print(ans)
