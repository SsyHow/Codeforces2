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
    a, b, c, d = MII()

    if a*d ==  b * c:
        print(0)
    elif (a!= 0 and (b*c) % (a*d)) == 0 or (c != 0 and (a * d) % (b * c) == 0):
        print(1)
    else:
        print(2)