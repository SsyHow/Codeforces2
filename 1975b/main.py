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
    L.sort()

    k1 = L[0]
    f = True
    k2 = 0
    for i in L:
        if f and i % k1 != 0:
            k2 = i
            f = False
        elif i % k1 == 0 or i % k2 == 0:
            continue
        else:
            print("NO")
            break
    else:
        print("YES")