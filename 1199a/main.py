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
n, x, y = MII()
L = LII()

for i in range(n):
    v = True
    for j in range(max(0, i - x), i):
        if L[j] <= L[i]:
            v = False
            break

    for j in range(i + 1, i + y + 1):
        if j < n and L[j] <= L[i]:
            v = False
            break

    if v:
        print(i + 1)
        break