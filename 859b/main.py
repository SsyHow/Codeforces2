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

k = int(a ** 0.5)

if k ** 2 >= a:
    print(4 * k)
elif k * (k + 1) >= a:
    print(2 * (2 * k + 1))
else:
    print(4 * (k + 1))
