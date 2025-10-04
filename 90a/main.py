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
a, b, c = MII()

a = (a + 1) // 2
b = (b + 1) // 2
c = (c + 1) // 2

print(max((a - 1) * 3, (b - 1) * 3 + 1, (c - 1) * 3 + 2) + 30)
