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
off = 0
for _ in range(a):
    b = II()

    if b & 1 == 0:
        print(b // 2)

    elif off == 0:
        print(b // 2)
        off += 1
    elif off == 1:
        print(b // 2 + 1)
        off -= 1

