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
    b = II()
    prev = 0
    mmax = 0
    ans = []
    pmax = []

    L = LII()
    k = sum(L)
    for i in L:
        prev += i
        ans.append(prev)
        mmax = max(mmax, i)
        pmax.append(mmax)
    cnt = []
    for i in range(b):
        cnt.append(pmax[i] + k - ans[i])
    print(*cnt[::-1])
