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

L = [True] * 40004

for i in range(2, 40004):
    if L[i]:
        k = i
        while k < 40004 - i:
            k += i

            L[k] = False


a = II()
for _ in range(a):
    b = II()
    x = b + 1
    while not L[x]:
        x += 1
    y = x + b
    while not L[y]:
        y += 1
    print(x  *  y)