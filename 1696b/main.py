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
    L = LII()

    p0, p1 = 0, b - 1

    while p0 <= p1 and L[p0] == 0:
        p0 += 1
    while p0 <= p1 and L[p1] == 0:
        p1 -= 1

    if p0 > p1:
        print(0)
    elif 0 not in L[p0:p1+1]:
        print(1)
    else:
        print(2)
