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
n, a, x, b, y = MII()
a -= 1
x -= 1
b -= 1
y -= 1

while a != x and b != y:
    a = (a + 1) % n
    b = (b - 1) % n
    if a == b:
        print("YES")
        break
else:
    print("NO")