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
    L.append(list(I()))
f = True
for i in range(a):
    for j in range(a):
        cnt = 0
        if i > 0 and L[i - 1][j] == 'o':
            cnt += 1
        if i < a - 1 and L[i + 1][j] == 'o':
            cnt += 1
        if j > 0 and L[i][j - 1] == 'o':
            cnt += 1
        if j < a - 1 and L[i][j + 1] == 'o':
            cnt += 1

        if cnt & 1 == 1:
            f = False
print("YES" if f else "NO")