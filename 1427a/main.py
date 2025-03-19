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

    neg = []
    pos = []
    z = 0
    k = 0
    for i in L:
        if i < 0:
            neg.append(i)
        elif i > 0:
            pos.append(i)
        else:
            z += 1
        k += i
    if k == 0:
        print("NO")
        continue
    print("YES")
    if k > 0:
        print(*pos, *neg, *([0] * z))
    else:
        print(*neg, *pos, *([0] * z))

