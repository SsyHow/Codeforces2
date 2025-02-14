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
prev = -1
for i in range(1, a+1):
    b = II()
    if prev == -1:
        print(b - 1)
        prev = b-1
        continue

    if b - i >= prev + 1:
        print(b - i)
    else:
        print(prev + 1)

    prev = max(b - i,prev + 1 )


