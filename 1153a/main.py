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
ans = 1
cnt = float('inf')
for i in range(n):
    x, y = MII()
    if k <= x:
        tmp = x - k
    else:
        tmp = (k - x + y - 1) // y * y  + x - k
    if tmp < cnt:
        ans = i + 1
        cnt = tmp
print(ans)