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
for _ in range(a):
    b = II()
    if b == 1:
        print(1)
    elif b == 2:
        print(1, 2)
    else:
        k = 4
        L = [0] * b
        L[0] = 2
        L[b - 1] = 3
        L[b//2] = 1
        for i in range(b):
            if L[i] == 0:
                L[i] = k
                k += 1
        print(*L)