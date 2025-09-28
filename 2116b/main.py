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
mod = 998244353
max_bit = 100000
pow2 = [1] * (max_bit + 1)
for i in range(1, max_bit + 1):
    pow2[i] = (pow2[i - 1] * 2) % mod

for _ in range(a):
    b = II()
    L1 = LII()
    L2 = LII()

    ans = []
    loc1 = loc2 = 0
    for idx in range(b):
        if L1[loc1] < L1[idx]:
            loc1 = idx
        if L2[loc2] < L2[idx]:
            loc2 = idx

        x1, y1 = L1[loc1], L2[idx - loc1]
        if x1 < y1:
            x1, y1 = y1, x1

        x2, y2 = L2[loc2], L1[idx - loc2]
        if x2 < y2:
            x2, y2 = y2, x2
        if x1 > x2 or (x1 == x2 and y1 > y2):
            ans.append((pow2[x1] + pow2[y1]) % mod)
        else:
            ans.append((pow2[x2] + pow2[y2]) % mod)

    print(*ans)