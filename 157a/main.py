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
L = [LII() for _ in range(a)]

ans = 0
for i in range(a):
    for j in range(a):
        if sum(L[x][j] for x in range(a)) > sum([L[i][x] for x in range(a)]) :
            ans += 1
print(ans)