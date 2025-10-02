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
L = [True] * a
M = []
for i in range(a):
    x, y, z, b = MII()
    for j in range(len(M)):
        if not L[j]:
            continue
        x1, y1, z1, b1, _ = M[j]
        if x < x1 and y < y1 and z < z1:
            L[i] = False
        elif x > x1 and y > y1 and z > z1:
            L[j] = False
    M.append([x, y, z, b, i + 1])

ans = (float('inf'), 0)
for i in range(a):
    if L[i]:
        if M[i][3] < ans[0]:
            ans = M[i][3], M[i][4]
print(ans[1])
