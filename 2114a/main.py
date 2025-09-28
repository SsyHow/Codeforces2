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
    b = I()
    k = int(b)
    c = int(k ** 0.5)
    if c == 0 and k == 0 :
        print(0, 0)

    elif k // c == c and k % c == 0:
        print(0, c)
    else:
        print(-1)