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
for i in range(a):
    L.append(list(I()))
ans = 0
for i in range(a-1):
    for j in range(b-1):
        if set([L[i][j], L[i][j+1], L[i+1][j], L[i+1][j+1]]) == {'f', 'a', 'c', 'e'}:
            ans += 1
print(ans)