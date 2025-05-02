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
L = []
for _ in range(a):
    L.append(LII())
ans = 0
n = len(L)
for i in range(n):
    t, b, l, r = 0, 0, 0, 0

    for j in range(n):
        if L[i][0] == L[j][0]:
            if L[i][1] > L[j][1]:
                b = 1
            if L[i][1] < L[j][1]:
                t = 1
        if L[i][1] == L[j][1]:
            if L[i][0] > L[j][0]:
                r = 1
            if L[i][0] < L[j][0]:
                l = 1
    if t + b + l + r == 4:
        ans += 1
print(ans)
