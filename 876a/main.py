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
a = II()
b = II()
c = II()
L = [a, b, c]
k = min([a, b])
m = min(L)
if n == 1:
    print(0)
elif m == k:
    print(k * (n - 1))
else:
    print(m * (n - 2) + k )
