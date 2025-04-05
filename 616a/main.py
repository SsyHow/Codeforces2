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

if len(a) < len(b):
    a = '0' * (len(b) - len(a)) + a
else:
    b = '0' * (len(a) - len(b)) + b

if a < b:
    print("<")
elif a > b:
    print(">")
else:
    print("=")