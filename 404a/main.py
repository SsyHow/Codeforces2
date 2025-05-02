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
k = L[0][0]
m = L[0][1]
for i in range(a):
    for j in range(a):
        if i == j and L[i][j] != k:
            f = False
        elif j == a - i - 1 and L[i][j] != k:
            f = False
        elif (i != j and j != a - i - 1) and L[i][j] != m:
            f = False
print("YES" if f and k != m else "NO")