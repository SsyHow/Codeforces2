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

    if b < 5:
        print(-1)
        continue
    for i in range(2, b + 1, 2):
        if i != 4:
            print(i, end=' ')
    print("4 5", end = ' ')
    for i in range(1, b + 1, 2):
        if i != 5:
            print(i, end = ' ')
    print()