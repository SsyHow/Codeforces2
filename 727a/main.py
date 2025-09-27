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
a, b = MII()
L = [b]

while b > a:
    if b & 1 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        print("NO")
        break

    L.append(b)
else:
    if b == a:
        print("YES")
        print(len(L))
        print(*L[::-1])
    else:
        print("NO")
