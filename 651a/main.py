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
a, b = MII()
ans =0
if a > 1 or b > 1:
    while a >= 1 and b >= 1:
        if a <= b:
            a += 1
            b -= 2
        else:
            a -= 2
            b += 1
        ans += 1
    print(ans)
else:
    print(0)