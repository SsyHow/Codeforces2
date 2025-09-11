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
t = II()
for _ in range(t):
    n, k = MII()
    L1 = LII()
    L2 = LII()
    s = -1
    for i in range(n):
        if L2[i] >= 0 and s == -1:
            s = L1[i] + L2[i]
        elif L2[i] >= 0 and L1[i] + L2[i] != s:
            print(0)
            break
    else:
        if s >= 0 and (s - max(L1) < 0 or s - min(L1) > k):
            print(0)
        elif s >= 0:
            print(1)
        else:
            print(k - (max(L1) - min(L1)) + 1)