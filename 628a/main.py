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
x = 0
ta = a
def check(n):
    return 1 << (n.bit_length() - 1)

while a > 1:
    k = check(a)
    x += k * b + (k // 2)
    a -= k // 2
print(x, ta* c)