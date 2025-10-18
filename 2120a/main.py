import sys

input = sys.stdin.readline


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
    l1, b1, l2, b2, l3, b3 = MII()

    if l1 == l2 == l3 == b1 + b2 + b3:
        print("YES")
    elif b1 == b2 == b3 == l1 + l2 + l3:
        print("YES")

    elif l1 + l2 == l1 + l3 == b1 == b2 + b3:
        print("YES")
    elif b1 + b2 == b1 + b3 == l1 == l2 + l3:
        print("YES")
    else:
        print("NO")