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
for _ in range(a):
    b, c = MII()
    L = LII()
    M = []
    k = list(zip(L, range(b)))
    k.sort()
    tmp = []
    ans = 1
    for i in range(1, b):
        if k[i - 1][1] + 1 != k[i][1]:
            ans += 1
    print("YES" if ans <= c else "NO")

