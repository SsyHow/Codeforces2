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
    L = [0] * b
    even = b if b & 1 == 0 else b - 1
    odd = 1
    for i in range(b):
        if i & 1 == 0:
            L[i] = odd
            odd += 2
        else:
            L[i] = even
            even -= 2
    print(*L)