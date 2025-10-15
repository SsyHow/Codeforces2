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
    b, c = MII()
    L = LII()
    L.sort(reverse=True)
    s = 0

    for i in range(b):
        s += L[i]
        if s < (i + 1) * c:
            print(i)
            break
    else:
        print(i  + 1)


