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
    if b <= 2:
        print(*range(1,b+1))
    else:
        if b & 1 == 0:
            L = list(range(1, b + 1))
            for i in range(0, b, 2):
                L[i], L[i+1] = L[i+1], L[i]
            print(*L)
        else:
            print(-1)