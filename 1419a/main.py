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
    s = I()

    if b & 1 == 1:
        for i in range(0, b, 2):
            if int(s[i]) & 1 == 1:
                print(1)
                break
        else:
            print(2)
    else:
        for i in range(1, b, 2):
            if int(s[i]) & 1 == 0:
                print(2)
                break
        else:
            print(1)
