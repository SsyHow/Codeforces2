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

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


r1, r2 = MII()
c1, c2 = MII()
d1, d2 = MII()

a = (r1 + c1 - d2) // 2
b = (r1 + d2 - c1) // 2
c = (c1 + r2 - d1) // 2
d = (c2 + d1 - r1) // 2
k = {a, b, c, d}
if a + b != r1 or c + d != r2 or a + c != c1 or b + d != c2 or a + d != d1 or b + c != d2:
    print(-1)

elif len(k) != 4 or any(i > 9  or i < 1 for i in k):
    print(-1)
else:
    print(a, b)
    print(c, d)