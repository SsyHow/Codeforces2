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

L.sort()

t = [0] * a
k = (a + 1) // 2
b = 0
for i in range(a):
    if i & 1 == 0:
        t[i] = L[b]
        b += 1
    else:
        t[i] = L[k]
        k += 1
print(*t)
