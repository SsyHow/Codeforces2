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
offset = a
for i in range(a+1):
    print(*([' '] * (offset - i) + list(range(i + 1))) + list(range(i - 1, -1, -1)))
for i in range((a - 1), -1, -1):
    print(*([' '] * (offset - i) + list(range(i + 1))) + list(range(i - 1, -1, -1)))
