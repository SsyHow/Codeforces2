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
    b, c, d = MII()
    c, d = sorted([c, d])
    if c != 0 or d == 0:
        print(-1)
    elif (b - 1) % d == 0:
        k = 1 + d + 1
        L = [1] * d
        for i in range(d, (b-1)):
            # print(k, d, i + 1)
            if k + d -1> i +1:
                L.append(k)
            else:
                k += d
                L.append(k)
        print(*L)

    else:
        print(-1)

