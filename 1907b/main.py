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

    L = list(I())
    n = len(L)
    B = []
    b = []

    for i in range(n):
        if L[i] == 'b':
            L[i] = ''
            if not b:
                continue
            x = b.pop()
            L[x] = ''

        elif 'a' <= L[i] <= 'z':
            b.append(i)

        if L[i] == 'B':
            L[i] = ''
            if not B:
                continue
            x = B.pop()
            L[x] = ''

        elif 'A' <= L[i] <= 'Z':
            B.append(i)
    print(''.join(L))