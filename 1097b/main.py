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
n = II()
L = []
for i in range(n):
    L.append(II())

for i in range(2 ** n):
    k = 0
    for j in range(n):
        if (i >> j) & 1 == 1:
            k += L[j]
        else:
            k -= L[j]

    if k % 360 == 0:
        print("YES")
        break
else:
    print("NO")

