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
a = I()
b = I()
c = I()

def f(x, y):
    if x == 'rock' and y == 'scissors':
        return True
    if x == 'scissors' and y == 'paper':
        return True
    if x == 'paper' and y == 'rock':
        return True
    return False

if a != b and b == c and f(a, b):
    print("F")
elif b != a and a == c and f(b, a):
    print("M")
elif c != b and a == b and f(c, b):
    print("S")
else:
    print("?")