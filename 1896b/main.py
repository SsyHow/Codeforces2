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

    p0 = 0
    p1 = b-1
    while p0 < b and s[p0] == 'B':
        p0 += 1
    while p1 >= 0 and s[p1] == 'A':
        p1 -=1

    print(max(p1 - p0, 0))


