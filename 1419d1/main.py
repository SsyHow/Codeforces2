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
L = LII()
L.sort(reverse=True)
M = [0] * a
k = 0
for i in range(0, a, 2):
    M[i] = L[k]
    k += 1

for i in range(1, a, 2):
    M[i] = L[k]
    k += 1

print((a + 1) // 2 - 1)

print(*M)