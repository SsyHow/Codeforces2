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
K = [1] * (a + 1)
K[0] = 0
for _ in range(a):
    L.append(LII())

for i in range(a):
    for j in range(a):
        if i == j:
            continue
        elif L[i][j] == 1:
            K[i+1] = 0
        elif L[i][j] == 2:
            K[j+1] = 0
        elif L[i][j] == 3:
            K[i+1] = 0
            K[j+1] = 0
print(sum(K))
print(*[idx for idx, i in enumerate(K) if i == 1])
