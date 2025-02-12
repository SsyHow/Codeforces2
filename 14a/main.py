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
L = [I() for _ in range(a)]

mini, minj, maxi, maxj = 50, 50, 0, 0

for i in range(a):
    for j in range(b):
        if L[i][j] == '*':
            mini, minj = min(mini, i), min(minj, j)
            maxi, maxj = max(maxi, i), max(maxj, j)
# print(mini, minj, maxi, maxj)
for i in range(a):
    if mini <= i <= maxi:
        print(L[i][minj:maxj+1])