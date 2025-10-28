import sys

input = lambda: sys.stdin.readline().rstrip()


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
    L = LI()
    if L.count('1') >= b // 2:
        if (b // 2) & 1 == 1 and L.count('1') >= b // 2 + 1:
            print(b // 2 + 1)
            print('1 ' * (b // 2 + 1))

        elif (b // 2) & 1 == 1:
            print(b // 2)
            print('0  ' * (b // 2))
        else:
            print(b // 2)
            print('1  ' * (b // 2))
    else:
        print(b // 2)
        print('0 ' * (b // 2))