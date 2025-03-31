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
s = I()
L = s.split()
k = int(L[0])
if L[2] == 'month':

    if k >= 31:
        print(7)

    elif k >= 30:
        print(11)
    else:
        print(12)
else:
    if k == 5 or k == 6:
        print(53)
    else:
        print(52)